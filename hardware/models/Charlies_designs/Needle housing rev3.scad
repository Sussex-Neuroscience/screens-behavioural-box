$fs = 0.1;
union(){
    difference(){
        union(){
            cylinder(h=15, d=3.9);
                    
            translate([0,0,1])
                cylinder(h=4, d1=3.9, d2=6);
            translate([0,0,5])
                cylinder(h=2, d=6);
            translate([0,0,10])
                cylinder(h=5,d1=4.4, d2=3.9);
        }
        cylinder(h=15, d=2.9);
        
        
        translate([-3,-0.3,10])
            cube([6,0.6,5]);
    }
    
    
        
       
    
}

    