
difference(){
    union(){
        cylinder(h=10, d=18.2);
        translate([0,0,10])
            cylinder(h=8, d=25);
        
    }
    translate([2,2,0])
        cylinder(h=20, d=2);
    translate([-2,2,0])
        cylinder(h=20, d=2);
    translate([2,-2,0])
        cylinder(h=20, d=2);
    translate([-2,-2,0])
        cylinder(h=20, d=2);
}