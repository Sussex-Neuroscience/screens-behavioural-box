union(){
    //Base Layer
    difference(){
        $fs = 0.4;
        //Base
        translate([-1,-1,-11])
            cube([130,110,5]);
        //PCB1 Holes
        translate([5,5,-7])
            cylinder(h=3, d=3);
        translate([5,82,-7])
            cylinder(h=3, d=3);
        translate([72,5,-7])
            cylinder(h=3, d=3);
        translate([72,82,-7])
            cylinder(h=3, d=3);
        
        //PCB2 Holes
        translate([82.1,5,-7])
            cylinder(h=3, d=3);
        translate([82.1,46.35,-7])
            cylinder(h=3, d=3);
        translate([120.4,5,-7])
            cylinder(h=3, d=3);
        translate([120.4,46.35,-7])
            cylinder(h=3, d=3);
        //PCB3 Holes
        translate([82.1,56.35,-7])
            cylinder(h=3, d=3);
        translate([82.1,97.7,-7])
            cylinder(h=3, d=3);
        translate([120.4,56.35,-7])
            cylinder(h=3, d=3);
        translate([120.4,97.7,-7])
            cylinder(h=3, d=3);
        
        
        }

    //North Wall
    difference(){
        translate([-1,-2,-11])
            cube([130,1,35]);
        translate([37.82,-6,7])
            cube([8,5,3]);
    }
    //East Wall
    difference(){
        translate([-2,-6,-11])
            cube([1,115,35]);
        translate([-6,68,-4.5])
            cube([5,10,11.5]);
    }
    //South Wall ---Create hole for cable outlets 
    difference(){
        translate([-2,109,-11])
            cube([132,1,35]);
        translate([33.75,109,10])
            rotate([270,0,0])
            cylinder(h=5, d=15);
        translate([101.25,109,10])
            rotate([270,0,0])
            cylinder(h=5, d=15);
    }
    //West Wall
    translate([129,-2,-11])
        cube([1,112,35]);
}