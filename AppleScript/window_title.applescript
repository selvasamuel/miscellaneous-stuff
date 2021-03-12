-- This script prints the name of the application that is currently at the front
-- as well as the title of the window in that application that has the focus.
-- 
-- To run this script, execute the following command in Terminal: osascript window_title.applescript
-- 
-- When you run the script for the first time, Terminal will guide you through the steps you need to take to give appropriate permissions to the script.
-- On subsequent runs, you need to do the following to make sure that the script has the required permissions:
-- 1. Go to System Preferences > Security & Privacy > Accessibility. Click on "Click the lock to make changes." and enter your password.
--    Add Terminal to the list by clicking on + and make sure that the check box to the left of the entry corresponding to the Terminal
--    app is selected.
-- 2. Go to System Preferences > Security & Privacy > Automation. Make sure that the check box to the left of the entry System Events.app
--    under Terminal is selected.
-- 
-- After running the script, remove the permissions that you granted to Terminal.
-- 
-- Reference: https://stackoverflow.com/questions/5292204/macosx-get-foremost-window-title
repeat
    tell application "System Events"
        set frontApp to first application process whose frontmost is true
        set frontAppName to name of frontApp
        log frontAppName

        tell process frontAppName
            tell (1st window whose value of attribute "AXMain" is true)
                set windowTitle to value of attribute "AXTitle"
                log windowTitle
            end tell
        end tell
    end tell
end repeat
