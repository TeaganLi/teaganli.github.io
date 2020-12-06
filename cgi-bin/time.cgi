#!/export/local/bin/perl
print "Content-type: text/html\n\n";
print "<html><head><title>The current time is:</title></head>\n";
print `date`;
