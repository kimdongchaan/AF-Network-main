rule Tor_test
{
    strings:
        $s1= /http:\/\/[1-z]*.onion/
    condition:
        $s1
}