//we need a serial parsing library: https://github.com/kroimon/Arduino-SerialCommand
#include <SerialCommand.h>

#define relay1 16
#define relay2 17
#define relay3 05
#define relay4 18
#define touch_pin1 12
#define touch_pin2 13
#define touch_pin3 14
#define touch_pin4 27

int threshold_value = 250;

SerialCommand sCmd;     // The demo SerialCommand object

void setup() {
  // put your setup code here, to run once:
pinMode(relay1,OUTPUT);
pinMode(relay2,OUTPUT);
pinMode(relay3,OUTPUT);
pinMode(relay4,OUTPUT);

//pinMode(touch_pin1,INPUT);
//pinMode(touch_pin2,INPUT);
//pinMode(touch_pin3,INPUT);
//pinMode(touch_pin4,INPUT);

Serial.begin(115200);
  // generic functions for development/understanding the parsing library
  sCmd.addCommand("HELLO", sayHello);        // Echos the string argument back
  sCmd.addCommand("P",     processCommand);  // Converts two arguments to integers and echos them back
  sCmd.setDefaultHandler(unrecognized);      // Handler for command that isn't matched  (says "What?")



  sCmd.addCommand("rew1", reward1); // activate reward routine (reward 10) // start reward routine on relay1
  sCmd.addCommand("rew2", reward2);
  sCmd.addCommand("rew3", reward3);
  sCmd.addCommand("rew4", reward4);

  sCmd.addCommand("touch1", touch1);
  sCmd.addCommand("touch2", touch2);
  sCmd.addCommand("touch3", touch3);
  sCmd.addCommand("touch4", touch4);
}

void loop() {
  // put your main code here, to run repeatedly:
  sCmd.readSerial();     // We don't do much, just process serial commands


}//end void loop

//_____________________________________________________________________________________________________
void reward1(){
  char *arg;
  int time;
  arg = sCmd.next();
  if (arg != NULL) {
     time = atoi(arg);}
  else{time=50;}

  //Serial.println("rewardA");
  digitalWrite(relay1,HIGH);
  delay(time);
  digitalWrite(relay1,LOW);
     
}//end Reward

void reward2(){
  char *arg;
  int time;
  arg = sCmd.next();
  if (arg != NULL) {
     time = atoi(arg);}
  else{time=50;}
  //Serial.println("rewardA");
  digitalWrite(relay2,HIGH);
  delay(time);
  digitalWrite(relay2,LOW);
     
}//end Reward2

void reward3(){
  char *arg;
  int time;
  arg = sCmd.next();
  if (arg != NULL) {
     time = atoi(arg);}
  else{time=50;}
  //Serial.println("rewardA");
  digitalWrite(relay3,HIGH);
  delay(time);
  digitalWrite(relay3,LOW);
     
}//end Reward3

void reward4(){
  char *arg;
  int time;
  arg = sCmd.next();
  if (arg != NULL) {
     time = atoi(arg);}
  else{time=50;}
  //Serial.println("rewardA");
  digitalWrite(relay4,HIGH);
  delay(time);
  digitalWrite(relay4,LOW);
     
}//end Reward4

void touch1(){
  int touch_data;
  touch_data = touchRead(touch_pin1);
  Serial.println(touch_data);


}


void touch2(){
  int touch_data;
  touch_data = touchRead(touch_pin2);
  Serial.println(touch_data);


}


void touch3(){
  int touch_data;
  touch_data = touchRead(touch_pin3);
  Serial.println(touch_data);


}


void touch4(){
  int touch_data;
  touch_data = touchRead(touch_pin4);
  Serial.println(touch_data);


}


//_______________________________________________________________________________________________________________


void sayHello() {

  char *arg;
  arg = sCmd.next();    // Get the next argument from the SerialCommand object buffer
  if (arg != NULL) {    // As long as it existed, take it
    Serial.print("Hello ");
    Serial.println(arg);
  }
  else {
    Serial.println("Hello, whoever you are");
  }
}

void processCommand() {
  int aNumber;
  char *arg;

  Serial.println("We're in processCommand");
  arg = sCmd.next();
  if (arg != NULL) {
    aNumber = atoi(arg);    // Converts a char string to an integer
    Serial.print("First argument was: ");
    Serial.println(aNumber);
  }
  else {
    Serial.println("No arguments");
  }

  arg = sCmd.next();
  if (arg != NULL) {
    aNumber = atol(arg);
    Serial.print("Second argument was: ");
    Serial.println(aNumber);
  }
  else {
    Serial.println("No second argument");
  }
}

// This gets set as the default handler, and gets called when no other command matches.
void unrecognized(const char *command) {
  Serial.println("What?");
}
