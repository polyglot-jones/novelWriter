# -*- coding: utf-8 -*-
"""novelWriter Project Item Status Class

 novelWriter – Project Item Status Class
=========================================
 Class holding the status elements of a project item

 File History:
 Created: 2019-05-19 [0.1.3]

 This file is a part of novelWriter
 Copyright 2020, Veronica Berglyd Olsen

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful, but
 WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import logging

from lxml import etree

from nw.common import checkInt

logger = logging.getLogger(__name__)

class NWStatus():

    def __init__(self):
        self.theLabels  = []
        self.theColours = []
        self.theCounts  = []
        self.theMap     = {}
        self.theLength  = 0
        self.theIndex   = 0
        return

    def addEntry(self, theLabel, theColours):
        """Add a status entry to the status object, but ensure it isn't
        a duplicate.
        """
        theLabel = theLabel.strip()
        if self.lookupEntry(theLabel) is None:
            self.theLabels.append(theLabel)
            self.theColours.append(theColours)
            self.theCounts.append(0)
            self.theMap[theLabel] = self.theLength
            self.theLength += 1
        return True

    def lookupEntry(self, theLabel):
        """Look up a status entry in the object lists, and return it if
        it exists.
        """
        if theLabel is None:
            return None
        theLabel = theLabel.strip()
        if theLabel in self.theMap.keys():
            return self.theMap[theLabel]
        return None

    def checkEntry(self, theStatus):
        """Check if a status value is valid, and returns the safe
        reference to be used internally.
        """
        if isinstance(theStatus, str):
            theStatus = theStatus.strip()
            if self.lookupEntry(theStatus) is not None:
                return theStatus
        theStatus = checkInt(theStatus, 0, False)
        if theStatus >= 0 and theStatus < self.theLength:
            return self.theLabels[theStatus]

    def setNewEntries(self, newList):
        """Update the list of entries after they have been modified by
        the GUI tool.
        """
        replaceMap = {}

        if newList is not None:
            self.theLabels  = []
            self.theColours = []
            self.theCounts  = []
            self.theMap     = {}
            self.theLength  = 0
            self.theIndex   = 0

            for nName, nR, nG, nB, oName in newList:
                self.addEntry(nName, (nR, nG, nB))
                if nName != oName and oName is not None:
                    replaceMap[oName] = nName

        return replaceMap

    def resetCounts(self):
        """Clear the counts of references to the status entries.
        """
        self.theCounts = [0]*self.theLength
        return

    def countEntry(self, theLabel):
        """Lookup the usage count of a given entry.
        """
        theIndex = self.lookupEntry(theLabel)
        if theIndex is not None:
            self.theCounts[theIndex] += 1
        return

    def packEntries(self, xParent):
        """Pack the status entries into an XML object for saving to the
        main project file.
        """
        for n in range(self.theLength):
            xSub = etree.SubElement(xParent, "entry", attrib={
                "blue"  : str(self.theColours[n][2]),
                "green" : str(self.theColours[n][1]),
                "red"   : str(self.theColours[n][0]),
            })
            xSub.text = self.theLabels[n]
        return True

    def unpackEntries(self, xParent):
        """Unpack an XML tree and set the class values.
        """
        theLabels  = []
        theColours = []

        for xChild in xParent:
            theLabels.append(xChild.text)
            if "red" in xChild.attrib:
                cR = checkInt(xChild.attrib["red"], 0, False)
            else:
                cR = 0
            if "green" in xChild.attrib:
                cG = checkInt(xChild.attrib["green"], 0, False)
            else:
                cG = 0
            if "blue" in xChild.attrib:
                cB = checkInt(xChild.attrib["blue"], 0, False)
            else:
                cB = 0
            theColours.append((cR, cG, cB))

        if len(theLabels) > 0:
            self.theLabels  = []
            self.theColours = []
            self.theCounts  = []
            self.theMap     = {}
            self.theLength  = 0
            self.theIndex   = 0

            for n in range(len(theLabels)):
                self.addEntry(theLabels[n], theColours[n])

        return True

    ##
    #  Iterator Bits
    ##

    def __getitem__(self, n):
        """Return an entry by its index.
        """
        if n >= 0 and n < self.theLength:
            return self.theLabels[n], self.theColours[n], self.theCounts[n]
        return None, None, None

    def __iter__(self):
        """Initialise the iterator.
        """
        self.theIndex = 0
        return self

    def __next__(self):
        """Return the next entry for the iterator.
        """
        if self.theIndex < self.theLength:
            theLabel, theColour, theCount = self.__getitem__(self.theIndex)
            self.theIndex += 1
            return theLabel, theColour, theCount
        else:
            raise StopIteration

# END Class NWStatus
