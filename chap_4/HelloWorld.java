class HelloWorld{
  public static void main(String args[]){
    int x = 17;
    String name = "Happy";
    x = x*2;
    System.out.println("The New Value of x is: " +x );
    for(int i=0; i<10; i++){
      if((i==5) && (name.equals("Happy"))){
        System.out.println("Hell Yeah");
      }
      else
          System.out.print("The value of i is:" +i +"\n");
    }
  }
}
