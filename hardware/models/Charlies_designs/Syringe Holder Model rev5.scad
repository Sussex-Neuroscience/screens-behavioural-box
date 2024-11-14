union(){
    $fs = 0.5;
    difference(){
        translate([-2.5,0,0.5])
            cube([8,20,5.5]);
        translate([1.5,5,0.5])    
            cylinder(h=5.5, d=4);
        translate([1.5,15,0.5])    
            cylinder(h=5.5, d=4);
    }
    difference(){
        translate([-2.5,0,5.5])
            cube([8,20,3]);
        translate([1.5,5,5.5])
            cylinder(h=3, d=5.5);
        translate([1.5,15,5.5])
            cylinder(h=3, d=5.5);  
    }
    translate([1.5,-3,20])
        rotate([270,0,0])
        difference(){
            cylinder(h=3, d=26);
            cylinder(h=3, d=20);
            }
    difference(){
        translate([1.5,0,20])
            rotate([270,0,0])
            difference(){
                cylinder(h=20, d=26);
                cylinder(h=20, d=21.8);
            }
        translate([1.5,5,7])
            rotate([0,0,0])
            cylinder(h=30, d=8);  
        translate([1.5,15,7])
            rotate([0,0,0])
            cylinder(h=30, d=8);
    }       
}

