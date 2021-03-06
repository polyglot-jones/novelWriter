# -*- coding: utf-8 -*-
"""novelWriter GUI Document Details

 novelWriter – GUI Document Details
====================================
 Class holding the left side document details panel

 File History:
 Created: 2019-04-24 [0.0.1]

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
import nw

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from nw.constants import (
    nwLabels, nwItemClass, nwItemType, nwItemLayout
)

logger = logging.getLogger(__name__)

class GuiItemDetails(QWidget):

    def __init__(self, theParent):
        QWidget.__init__(self, theParent)

        logger.debug("Initialising GuiItemDetails ...")
        self.mainConf   = nw.CONFIG
        self.theParent  = theParent
        self.theProject = theParent.theProject
        self.theTheme   = theParent.theTheme
        self.theHandle  = None

        self.mainBox = QGridLayout(self)
        self.mainBox.setVerticalSpacing(1)
        self.mainBox.setHorizontalSpacing(6)
        self.setLayout(self.mainBox)

        self.pS = 0.9*self.theTheme.fontPointSize
        self.iPx = self.theTheme.baseIconSize
        self.sPx = int(round(0.8*self.theTheme.baseIconSize))

        self.expCheck = self.theTheme.getPixmap("check", (self.iPx, self.iPx))
        self.expCross = self.theTheme.getPixmap("cross", (self.iPx, self.iPx))

        self.fntLabel = QFont()
        self.fntLabel.setBold(True)
        self.fntLabel.setPointSizeF(self.pS)

        self.fntValue = QFont()
        self.fntValue.setPointSizeF(self.pS)

        # Label
        self.labelName = QLabel("Label")
        self.labelName.setFont(self.fntLabel)
        self.labelName.setAlignment(Qt.AlignLeft | Qt.AlignBaseline)

        self.labelFlag = QLabel("")
        self.labelFlag.setAlignment(Qt.AlignRight | Qt.AlignBaseline)

        self.labelData = QLabel("")
        self.labelData.setFont(self.fntValue)
        self.labelData.setAlignment(Qt.AlignLeft | Qt.AlignBaseline)
        self.labelData.setWordWrap(True)

        # Status
        self.statusName = QLabel("Status")
        self.statusName.setFont(self.fntLabel)
        self.statusName.setAlignment(Qt.AlignLeft)

        self.statusFlag = QLabel("")
        self.statusFlag.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.statusData = QLabel("")
        self.statusData.setFont(self.fntValue)
        self.statusData.setAlignment(Qt.AlignLeft)

        # Class
        self.className = QLabel("Class")
        self.className.setFont(self.fntLabel)
        self.className.setAlignment(Qt.AlignLeft)

        self.classFlag = QLabel("")
        self.classFlag.setFont(self.fntValue)
        self.classFlag.setAlignment(Qt.AlignRight)

        self.classData = QLabel("")
        self.classData.setFont(self.fntValue)
        self.classData.setAlignment(Qt.AlignLeft)

        # Layout
        self.layoutName = QLabel("Layout")
        self.layoutName.setFont(self.fntLabel)
        self.layoutName.setAlignment(Qt.AlignLeft)

        self.layoutFlag = QLabel("")
        self.layoutFlag.setFont(self.fntValue)
        self.layoutFlag.setAlignment(Qt.AlignRight)

        self.layoutData = QLabel("")
        self.layoutData.setFont(self.fntValue)
        self.layoutData.setAlignment(Qt.AlignLeft)

        # Character Count
        self.cCountName = QLabel("  Characters")
        self.cCountName.setFont(self.fntLabel)
        self.cCountName.setAlignment(Qt.AlignRight)

        self.cCountData = QLabel("")
        self.cCountData.setFont(self.fntValue)
        self.cCountData.setAlignment(Qt.AlignRight)

        # Word Count
        self.wCountName = QLabel("  Words")
        self.wCountName.setFont(self.fntLabel)
        self.wCountName.setAlignment(Qt.AlignRight)

        self.wCountData = QLabel("")
        self.wCountData.setFont(self.fntValue)
        self.wCountData.setAlignment(Qt.AlignRight)

        # Paragraph Count
        self.pCountName = QLabel("  Paragraphs")
        self.pCountName.setFont(self.fntLabel)
        self.pCountName.setAlignment(Qt.AlignRight)

        self.pCountData = QLabel("")
        self.pCountData.setFont(self.fntValue)
        self.pCountData.setAlignment(Qt.AlignRight)

        # Assemble
        self.mainBox.addWidget(self.labelName,  0, 0, 1, 1)
        self.mainBox.addWidget(self.labelFlag,  0, 1, 1, 1)
        self.mainBox.addWidget(self.labelData,  0, 2, 1, 3)

        self.mainBox.addWidget(self.statusName, 1, 0, 1, 1)
        self.mainBox.addWidget(self.statusFlag, 1, 1, 1, 1)
        self.mainBox.addWidget(self.statusData, 1, 2, 1, 1)
        self.mainBox.addWidget(self.cCountName, 1, 3, 1, 1)
        self.mainBox.addWidget(self.cCountData, 1, 4, 1, 1)

        self.mainBox.addWidget(self.className,  2, 0, 1, 1)
        self.mainBox.addWidget(self.classFlag,  2, 1, 1, 1)
        self.mainBox.addWidget(self.classData,  2, 2, 1, 1)
        self.mainBox.addWidget(self.wCountName, 2, 3, 1, 1)
        self.mainBox.addWidget(self.wCountData, 2, 4, 1, 1)

        self.mainBox.addWidget(self.layoutName, 3, 0, 1, 1)
        self.mainBox.addWidget(self.layoutFlag, 3, 1, 1, 1)
        self.mainBox.addWidget(self.layoutData, 3, 2, 1, 1)
        self.mainBox.addWidget(self.pCountName, 3, 3, 1, 1)
        self.mainBox.addWidget(self.pCountData, 3, 4, 1, 1)

        self.mainBox.setColumnStretch(0, 0)
        self.mainBox.setColumnStretch(1, 0)
        self.mainBox.setColumnStretch(2, 1)
        self.mainBox.setColumnStretch(3, 0)
        self.mainBox.setColumnStretch(4, 0)

        # Make sure the columns for flags and counts don't resize too often
        flagWidth  = self.theTheme.getTextWidth("Mm", self.fntValue)
        countWidth = self.theTheme.getTextWidth("99,999", self.fntValue)
        self.mainBox.setColumnMinimumWidth(1, flagWidth)
        self.mainBox.setColumnMinimumWidth(4, countWidth)

        logger.debug("GuiItemDetails initialisation complete")

        return

    ###
    #  Class Methods
    ##

    def updateCounts(self, tHandle, cC, wC, pC):
        """Just update the counts if the handle is the same as the one
        we're already showing.
        """
        if tHandle == self.theHandle:
            self.cCountData.setText("{:n}".format(cC))
            self.wCountData.setText("{:n}".format(wC))
            self.pCountData.setText("{:n}".format(pC))
        return

    def updateViewBox(self, tHandle):
        """Populate the details box from a given handle.
        """
        self.theHandle = tHandle
        nwItem = self.theProject.projTree[tHandle]

        if nwItem is None:
            self.labelFlag.setText("")
            self.labelData.setText("")
            self.statusFlag.setText("")
            self.statusData.setText("")
            self.classFlag.setText("")
            self.classData.setText("")
            self.layoutFlag.setText("")
            self.layoutData.setText("")
            self.cCountData.setText("–")
            self.wCountData.setText("–")
            self.pCountData.setText("–")

        else:
            theLabel = nwItem.itemName
            if len(theLabel) > 100:
                theLabel = theLabel[:96].rstrip()+" ..."

            iStatus = nwItem.itemStatus
            if nwItem.itemClass == nwItemClass.NOVEL:
                iStatus  = self.theProject.statusItems.checkEntry(iStatus) # Make sure it's valid
                flagIcon = self.theParent.statusIcons[iStatus]
            else:
                iStatus  = self.theProject.importItems.checkEntry(iStatus) # Make sure it's valid
                flagIcon = self.theParent.importIcons[iStatus]

            if nwItem.itemType == nwItemType.FILE:
                if nwItem.isExported:
                    self.labelFlag.setPixmap(self.expCheck)
                else:
                    self.labelFlag.setPixmap(self.expCross)
            else:
                self.labelFlag.setPixmap(QPixmap(1, 1))
            self.statusFlag.setPixmap(flagIcon.pixmap(self.sPx, self.sPx))
            self.classFlag.setText(nwLabels.CLASS_FLAG[nwItem.itemClass])
            if nwItem.itemLayout == nwItemLayout.NO_LAYOUT:
                self.layoutFlag.setText("-")
            else:
                self.layoutFlag.setText(nwLabels.LAYOUT_FLAG[nwItem.itemLayout])

            self.labelData.setText(theLabel)
            self.statusData.setText(nwItem.itemStatus)
            self.classData.setText(nwLabels.CLASS_NAME[nwItem.itemClass])
            self.layoutData.setText(nwLabels.LAYOUT_NAME[nwItem.itemLayout])

            if nwItem.itemType == nwItemType.FILE:
                self.cCountData.setText("{:n}".format(nwItem.charCount))
                self.wCountData.setText("{:n}".format(nwItem.wordCount))
                self.pCountData.setText("{:n}".format(nwItem.paraCount))
            else:
                self.cCountData.setText("–")
                self.wCountData.setText("–")
                self.pCountData.setText("–")

        return

# END Class GuiItemDetails
