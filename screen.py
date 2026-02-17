var1="""Workstation.GetScreenResolution MonitorNumber: 1 MonitorWidth => MonitorWidth MonitorHeight => MonitorHeight
SET varx TO %MonitorWidth% / 8
SET vary TO %MonitorHeight% / 6
Display.ShowMessageDialog.ShowMessage Title: $'''x,y''' Message: $'''%varx% , %vary%''' Icon: Display.Icon.None Buttons: Display.Buttons.OK DefaultButton: Display.DefaultButton.Button1 IsTopMost: False ButtonPressed=> ButtonPressed
"""
print("\033c\033[40;37m\n give me x div by screen' ? ")
a=input().strip()
print("\033[40;37m\n give me y div by screen  ")
b=input().strip()
var1=var1.replace("$0",a)
var1=var1.replace("$1",b)
print("\n"+"-"*80 +"\n")
print(var1)
