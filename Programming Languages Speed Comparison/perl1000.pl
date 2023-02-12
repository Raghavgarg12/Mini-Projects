use Time::HiRes qw( time );
open(fh, "1GB.txt") or die "Not opening";
my $start = time();
while(<fh>){
$UPPER_STRING = uc($_);
}
my $end = time();
printf("Perl :%.2f s\n", $end - $start);
open(w, ">>", "perl.txt");
print w ("\n",$end - $start);
close(w);