sourceDir = getDirectory("Choose source directory ");
destinationDir = getDirectory("Choose destination directory ");


var tiffFilePaths = newArray();
var	zipFilePaths = newArray();
var tempZipFilePaths = newArray();
var truncatedZipFilePaths = newArray();
var matchedPathPairs = newArray();
var ROInames = newArray();
var ROIindices = newArray();
var areaIndex = newArray();

setBatchMode("true");
count = 0;
countFiles(sourceDir);
n = 0;
print(count+" files processed");

scanFiles(sourceDir);

// Define the directory-searching function
function countFiles(sourceDir) {
	list = getFileList(sourceDir);
	for (i=0; i<list.length; i++) {
		if (endsWith(list[i], "/")) {
			countFiles(""+sourceDir+list[i]);
		} else {
			count++;
		}
	}
}

// Find all the files in the chosen directory
function scanFiles(sourceDir) {	
	list = getFileList(sourceDir);
	for (i=0; i<list.length; i++) {
		if (endsWith(list[i], "/")) {
			scanFiles(""+sourceDir+list[i]);
		} else {
			showProgress(n++, count);
			path = sourceDir+list[i];
			selectFiles(path);
		}
	}
}

// Find tiff files and zip files and send them to the sorting funcctions
function selectFiles(path) {
	filename = substring(path, (lastIndexOf(path, "/")+1));
	if (matches(filename, ".*[0-9]{4}[_][0-9][\\.][t][i][f]$||.*[0-9]{4}[_][0-9][0-9][\\.][t][i][f]$||.*[0-9]{4}[_][0-9][_][0-9][\\.][t][i][f]$||.*[0-9]{4}[_][0-9][0-9][_][0-9][\\.][t][i][f]$")) {
		tiffFilePath = path;
		tiffsArray(tiffFilePath);
	} else if (matches(filename, ".*[\\.][z][i][p]$")) {
		zipFilePath = path;
		zipsArray(zipFilePath);
	}
}

// Place all tiff file paths in tiff array
function tiffsArray(tiffFilePath) {
	tiffFilePaths = Array.concat(tiffFilePaths, tiffFilePath);
}

// Place all zip file paths in zip array
function zipsArray(zipFilePath) {
	zipFilePaths = Array.concat(zipFilePaths, zipFilePath);
}

// Place zip files that match tiff files into a temporary array
for (i=0; i<tiffFilePaths.length; i++) {
	tiffFileName = substring(tiffFilePaths[i], (lastIndexOf(tiffFilePaths[i], "/")+1));
	section = substring(tiffFileName, 0, lastIndexOf(tiffFileName, "."));
	for (j=0; j<zipFilePaths.length; j++) {
		zipFileName = substring(zipFilePaths[j], (lastIndexOf(zipFilePaths[j], "/")+1));
		zipName = substring(zipFileName, 0, (lastIndexOf(zipFileName, ".")));
		if (section == zipName) {
			tempZipFilePaths = Array.concat(tempZipFilePaths, zipFilePaths[j]);
			break;
		} else if (zipName == section+"_ind") {
			tempZipFilePaths = Array.concat(tempZipFilePaths, zipFilePaths[j]);
			break;
		}
	}
}

for (i=0; i<tempZipFilePaths.length; i++) {
	// Open the correct ROI zip for the tif
	roiManager("Open", tempZipFilePaths[i]);
	roiManager("show all");
	nR = roiManager("count");
	print("There are "+nR+" ROIs in "+substring(tempZipFilePaths[i], (lastIndexOf(tempZipFilePaths[i], "/")+1)));
	if (nR>0) {
		for (r=0; r<nR; r++) {
			rName = RoiManager.getName(r);
			if (matches(rName, "[a][r][e][a]|[dD][gG][_][rR]|[a][r][e][a][_][dD][gG][_][rR]|[dD][gG][_][lL]|[a][r][e][a][_][dD][gG][_][lL]")) {
				// print(substring(tempZipFilePaths[i], (lastIndexOf(tempZipFilePaths[i], "/")+1))+" has a DG region");
				truncatedZipFilePaths = Array.concat(truncatedZipFilePaths, tempZipFilePaths[i]);
				break;
			} else {
				print(substring(tempZipFilePaths[i], (lastIndexOf(tempZipFilePaths[i], "/")+1))+" has no DG regions.");
			}
		}
		roiManager("deselect");
		roiManager("delete");
		close("*");
	}
}

// Create an array of arrays (curated array of matched tiff and zip files)
for (z=0; z<truncatedZipFilePaths.length; z++) {
	zipFileName = substring(truncatedZipFilePaths[z], (lastIndexOf(truncatedZipFilePaths[z], "/")+1));
	section = substring(zipFileName, 0, (lastIndexOf(zipFileName, ".")));
	for (t=0; t<tiffFilePaths.length; t++) {
		tiffFileName = substring(tiffFilePaths[t], (lastIndexOf(tiffFilePaths[t], "/")+1));
		tiffName = substring(tiffFileName, 0, (lastIndexOf(tiffFileName, ".")));
		if (section == tiffName) {
			matchedPathPairs = Array.concat(matchedPathPairs, tiffFilePaths[t]);
			matchedPathPairs = Array.concat(matchedPathPairs, truncatedZipFilePaths[z]);
			break;
		} else if (section == tiffName+"_ind") {
			matchedPathPairs = Array.concat(matchedPathPairs, tiffFilePaths[t]);
			matchedPathPairs = Array.concat(matchedPathPairs, truncatedZipFilePaths[z]);
			break;
		}
	}
}

Array.show(matchedPathPairs);

for (i=0; i<(matchedPathPairs.length/2); i++) {
	// Open the correct image tif
	open(matchedPathPairs[(2*i)]);
	// Kill all colour channels
	Stack.setActiveChannels("0111");
	Stack.setActiveChannels("0011");
	Stack.setActiveChannels("0001");
	Stack.setActiveChannels("0000");
	// Open the correct ROI zip for the tif
	roiManager("Open", matchedPathPairs[(2*i)+1]);
	roiManager("show all");
	nR = roiManager("count");
	if (nR>0) {
		// Get array of all the ROI names
		for (r=0; r<nR; r++) {
			rName = RoiManager.getName(r);
			ROInames = Array.concat(ROInames, rName);
		}
		// Get array of all the ROI indices
		for (j=0; j<nR; j++) {
			roiManager("deselect");
			roiManager("select", j);
			j = roiManager("index");
			ROIindices = Array.concat(ROIindices, j);
			roiManager("deselect");
		}
		// Get array of the area ROI index
		for (k=0; k<nR; k++) {
				if (matches(ROInames[k], "[a][r][e][a]")) {
					areaIndex = Array.concat(areaIndex, k);
				} else if (matches(ROInames[k], "[dD][gG][_][rR]||[a][r][e][a][_][dD][gG][_][rR]|[dD][gG][_][lL]||[a][r][e][a][_][dD][gG][_][lL]")) {
					areaIndex = Array.concat(areaIndex, k);
				}
		}
		for (m=0; m<areaIndex.length; m++) {
			ROIindices = Array.deleteValue(ROIindices, areaIndex[m]);
		}
	}
	
	// Delete all ROIs except for the area ROI
	roiManager("deselect");
	roiManager("select", ROIindices);
	roiManager("delete");
	roiManager("deselect");
	
	// Change area ROI properties
	roiManager("Show All");
	RoiManager.setGroup(0);
	RoiManager.setPosition(1);
	roiManager("Set Color", "white");
	roiManager("Set Line Width", 10);
	
	// Create area PNG
	run("Flatten");
	roiName = substring(getTitle(), 0, lastIndexOf(getTitle(), "-")) + "_" + "area" + ".png";
	saveAs("PNG", destinationDir+roiName);
	
	// Reset and close
	areaIndex = newArray(0);
	ROInames = newArray(0);
	ROIindices = newArray(0);
	roiManager("deselect");
	roiManager("delete");
	close("*");
}
