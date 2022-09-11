unit ShutterCD;

{
Optical shutter using old CDROM drive
ShutterCD unit
Version 11.09.2022

(c) Serhiy Kobyakov
}


interface

uses
  Classes, SysUtils, dialogs, StdCtrls, Controls, Forms,
  IniFiles,
//  strutils,
  addfunc,
  ArduinoDevice;


type

  { ShutterCD_device }

  ShutterCD_device = Object (_ArduinoDevice)
    private

    public
      constructor Init(_ComPort: string);
      destructor Done;

      procedure Open;
      procedure Close;
  end;


implementation


constructor ShutterCD_device.Init(_ComPort: string);
var
  MyForm: TForm;
  MyLabel: TLabel;
//  AppIni: TIniFile;
//  iniFile: string;
  UpperInitStr: string;
begin
// -----------------------------------------------------------------------------
// the device ID string with which it responds to '?'
  theDeviceID := 'ShutterCD';
// -----------------------------------------------------------------------------
{
  iniFile := Application.Location + theDeviceID + '.ini';
  If not FileExists(iniFile) then
    begin
      showmessage('File ' + LineEnding + iniFile + LineEnding +
          'procedure ''' + {$I %CURRENTROUTINE%} + ''' failed!' + LineEnding +
          'File ' + iniFile + 'has not been found!' + LineEnding +
          'Please fix it');
      halt(0);
    end;
}

// make a splash screen
// which shows initialization process
  MyForm := TForm.Create(nil);
  with MyForm do begin
     SetBounds(0, 0, 450, 90); Position:=poDesktopCenter; BorderStyle := bsNone;
     MyForm.Color := $00EEEEEE; end;

  MyLabel := TLabel.Create(MyForm);
  with MyLabel do begin
     Autosize := True; Align := alNone; Alignment := taCenter; Parent := MyForm;
     Visible := True; AnchorVerticalCenterTo(MyForm);
     AnchorHorizontalCenterTo(MyForm); end;

  MyForm.Show; MyForm.BringToFront;
  UpperInitStr := 'Initializing ' + theDeviceID + ':' + LineEnding;

  MyLabel.Caption:= UpperInitStr + 'Reading ' + theDeviceID + '.ini...';
  sleepFor(50); // refresh the Label to see the change

// -----------------------------------------------------------------------------
// Read the device variables from ini file:
//  AppIni := TInifile.Create(iniFile);
// device-specific paremeters:


//  AppIni.Free;
// -----------------------------------------------------------------------------

// Use basic device initialization
  MyLabel.Caption:= UpperInitStr + 'Connecting to ' + _ComPort + '...';
  sleepFor(200); // refresh the Label to see the change
  Inherited Init(_ComPort);

// Set the shutter into the start position as a last step of initialization
  MyLabel.Caption:= UpperInitStr + 'Going to starting position...';
  sleepFor(50); // small delay to refresh the Label
  SendAndGetAnswer('i');

  MyLabel.Caption:= UpperInitStr + 'Done!';
  sleepFor(500); // refresh the Label just to see "Done"
  MyForm.Close;
  FreeAndNil(MyForm);
end;

destructor ShutterCD_device.Done;
begin
// I don't use the device answer here to improve reliability
// but SendAndGetAnswer returns '0' after 'o' if everything is OK
  SendCharAndGetAnswer('o');
  Inherited Done;
end;

procedure ShutterCD_device.Open;
begin
// I don't use the device answer here to improve reliability
// but SendAndGetAnswer returns '0' after 'o' if everything is OK
    SendCharAndGetAnswer('o');
end;

procedure ShutterCD_device.Close;
begin
// I don't use the device answer here to improve reliability
// but SendAndGetAnswer returns '0' after 'c' if everything is OK
    SendCharAndGetAnswer('c');
end;


end.


