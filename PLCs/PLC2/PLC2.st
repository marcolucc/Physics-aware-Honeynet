PROGRAM PLC2
  VAR
    level AT %IW0 : INT;
    request AT %QX0.0 : BOOL;
    open_req AT %MX0.0 : BOOL;
    close_req AT %MX0.1 : BOOL;
    low_2 AT %MW1 : INT := 10;
    high_2 AT %MW2 : INT := 20;
  END_VAR
  VAR
    LE10_OUT : BOOL;
    GE11_OUT : BOOL;
  END_VAR

  LE10_OUT := LE(level, low_2);
  open_req := LE10_OUT;
  GE11_OUT := GE(level, high_2);
  close_req := GE11_OUT;
  request := NOT(close_req) AND (open_req OR request);
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : PLC2;
  END_RESOURCE
END_CONFIGURATION
