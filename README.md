# kerbal Bad Apple
 bad apple played in ksp
 WORKFLOW TO GET THIS TO WORK.
 
 first I built an array of engines in ksp. anything should work, just note that the code pulls from the length and width coordinates (not the height).
 
 run 'krpc name change' with the craft file as input. this will make a new craft file that's used. Make sure to change the name of the craft in the craft file manually as well (first line) to prevent some bugs in game.
 
 'vid cutting' and 'imfolder reader' are both used to get the final data. vid cutting takes an mp4 and cuts the frames to jpg and imfolder reader takes a list of jpg and sets pixel on if pixel state switched between frames (an xor between frames to help with render time). Both these code bits are stolen and could be its own script.
 
 final: run 'ksp bad apple'
 ran using ksp 1.5.1 and krpc version 0.4.8
 
 other notes: theres one spot where the array for the engines is manually added. be sure to change that.
 theres no error protection so be careful. make sure that your initial video file is the same dimensions as your engine array.
 the final render for bad apple took about 9 hours, callingt he engines is slow, especially with large part crafts.