barD=3.2;
barL=300;
distance=234;

for (i=[0:10:distance]){
    
    rotate([0,0,0]){
        translate([i,0,0]){
cylinder(d=barD,h=barL);
        }//end translate
    }//end rotate
}//end for