PROGRAM PLC3
  VAR
    level AT %IW0 : INT;
    pump AT %QX0.0 : BOOL;
  END_VAR
  VAR
    low : BOOL;
  END_VAR
  VAR
    high AT %QX0.1 : BOOL;
  END_VAR
  VAR
    low_3 : INT := 0;
    high_3 : INT := 10;
    LE13_OUT : BOOL;
    GE12_OUT : BOOL;
  END_VAR

  LE13_OUT := LE(level, low_3);
  low := LE13_OUT;
  GE12_OUT := GE(level, high_3);
  high := GE12_OUT;
  pump := NOT(low) AND (high OR pump);
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : PLC3;
  END_RESOURCE
END_CONFIGURATION
