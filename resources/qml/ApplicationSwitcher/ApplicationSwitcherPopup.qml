// Copyright (c) 2021 Ultimaker B.V.
// Cura is released under the terms of the LGPLv3 or higher.

import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.15

import UM 1.4 as UM
import Cura 1.1 as Cura

Popup
{
    id: applicationSwitcherPopup

    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

    opacity: opened ? 1 : 0
    Behavior on opacity { NumberAnimation { duration: 100 } }
    padding: UM.Theme.getSize("wide_margin").width

    contentItem: Grid
    {
        id: ultimakerPlatformLinksGrid
        columns: 3
        spacing: UM.Theme.getSize("default_margin").width

        Repeater
        {
            model:
            [
                {
                    displayName: "FELIX Printers",
                    thumbnail: UM.Theme.getIcon("Felix-2", "high"),
                    description: "Visit felix website ",
                    link: "https://felixprinters.com/",
                    permissionsRequired: []
                },

                {
                    displayName: "Shop FELIX Printers",
                    thumbnail: UM.Theme.getIcon("Shop", "high"),
                    description: "Visit shop of the FELIX Printers ",
                    link: "https://shop.felixprinters.com/",
                    permissionsRequired: []
                },
                {
                    displayName: "Report bug",
                    thumbnail: UM.Theme.getIcon("Bug", "high"),
                    description: "If you find error feel free to report it. !Requires GithubAccount",
                    link: "https://github.com/FELIXroboticsBV/FELIX-FILO/issues/new?template=bugreport.yaml",
                    permissionsRequired: []
                },
                {
                    displayName: "Contact support",
                    thumbnail: UM.Theme.getIcon("Help", "high"),
                    description: "If you encounter any issue please contact our support !",
                    link: "mailto:support@felixprinters.com?cc=SPK@felixrobotics.com&subject=Problem(s)%20with%20FELIX%20Filo%20v1&body=Hi%20FELIX%20Printers%20team%2C%0A%0AI'd%20like%20to%20report%20an%20issue%20with%20FELIX%20FILO.%20Here%20are%20the%20details%3A%0A%0AFELIX%20FILO%20Version%3A%0A%5Be.g.%2C%201.0%20alpha%5D%0A%0AOperating%20System%3A%0A%5Be.g.%2C%20Windows%2011%20%2F%20macOS%20Catalina%20%2F%20MX%20Linux%20%E2%80%94%20please%20include%20GPU%20if%20relevant%5D%0A%0APrinter%3A%0A%5Be.g.%2C%20FELIX%20Pro%20L%20%2F%20FELIX%20Food%20Twin%20%E2%80%94%20please%20note%20if%20you've%20made%20any%20firmware%20modifications%5D%0A%0AReproduction%20Steps%3A%0A%0A%5BSomething%20you%20did%5D%0A%5BSomething%20you%20did%20next%5D%0A%5B...%5D%0A%0AActual%20Results%3A%0A%5BWhat%20happened%20after%20following%20the%20steps%20above%3F%5D%0A%0AExpected%20Results%3A%0A%5BWhat%20did%20you%20expect%20to%20happen%20instead%3F%5D%0A%0AAttachments%3A%0ADepending%20on%20the%20type%20of%20issue%2C%20please%20attach%20the%20following%3A%0A%0A-%20Print%20quality%20issue%3A%20A%20Project%20File%20(in%20FILO%2C%20go%20to%20File%20%E2%86%92%20Save%20Project).%20Please%20zip%20the%20file%20before%20attaching.%20G-code%20files%20are%20not%20project%20files.%20If%20the%20file%20is%20too%20large%20for%20email%2C%20please%20use%20WeTransfer%20or%20a%20similar%20service.%0A-%20UI%20%2F%20usability%20issue%3A%20Screenshots%20showing%20the%20issue%20%E2%80%94%20before%2Fafter%20shots%20with%20arrows%20are%20very%20helpful.%0A-%20Crash%20or%20unexpected%20behavior%3A%20Your%20log%20file%2C%20found%20at%3A%0AWindows%3A%20%25APPDATA%25%5Ccura%5C%3CFILO%20version%3E%5Ccura.log%0AmacOS%3A%20~%2FLibrary%2FApplication%20Support%2Fcura%2F%3CFILO%20version%3E%2Fcura.log%0ALinux%3A%20~%2F.local%2Fshare%2Fcura%2F%3CFILO%20version%3E%2Fcura.log%0A(You%20can%20also%20reach%20this%20folder%20via%20Help%20%E2%86%92%20Show%20Settings%20Folder%20in%20the%20app.)%0A%0AThank%20you!%0A%0A%5BYour%20Name%5D",
                    permissionsRequired: []
                }
            ]

            delegate: ApplicationButton
            {
                displayName: modelData.displayName
                iconSource: modelData.thumbnail
                tooltipText: modelData.description
                isExternalLink: true
                visible:
                {
                    try
                    {
                        modelData.permissionsRequired.forEach(function(permission)
                        {
                            if(!Cura.API.account.isLoggedIn || !Cura.API.account.permissions.includes(permission)) //This required permission is not in the account.
                            {
                                throw "No permission to use this application."; //Can't return from within this lambda. Throw instead.
                            }
                        });
                    }
                    catch(e)
                    {
                        return false;
                    }
                    return true;
                }

                onClicked: Qt.openUrlExternally(modelData.link)
            }
        }
    }

    background: UM.PointingRectangle
    {
        color: UM.Theme.getColor("tool_panel_background")
        borderColor: UM.Theme.getColor("lining")
        borderWidth: UM.Theme.getSize("default_lining").width

        // Move the target by the default margin so that the arrow isn't drawn exactly on the corner
        target: Qt.point(width - UM.Theme.getSize("default_margin").width - (applicationSwitcherButton.width / 2), -10)

        arrowSize: UM.Theme.getSize("default_arrow").width
    }
}
