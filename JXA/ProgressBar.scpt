JsOsaDAS1.001.00bplist00�Vscript_ObjC.import('Cocoa')
currentApp = Application.currentApplication()
currentApp.includeStandardAdditions = true

currentApp.displayAlert("Hello")

Progress.totalUnitCount = 5
Progress.description = "Hello"
for (i=0; i < 10; i++)
{
	Progress.completedUnitCount = i
	delay(1)
}	
                              ) jscr  ��ޭ