/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package shiftingandconverting;

/**
 *
 * @author Jamie
 */
public class conversions {
    private String group = "";
    private String output = "";
    String alph = "abcdefghijklmnopqrstuvwxyz";
    char[] alphabet = alph.toCharArray();           // creating an array of the alphabet character by character
    
    public void clear(){                            // this method resets string group and output to be empty again
        group = "";
        output = "";
    }
    
    public String ascii(String hex){                    // method to convert the hexadecimal values into ascii
        String hexString = hex;
        char[] charArray = hexString.toCharArray();     // creates an array of each hexadecimal value
        clear();                                        // makes sure strings group and output don't already contain data
        
        for(char c : charArray){
            if(c != ' '){
                group += c;
                
                if(group.length() == 2){
                    int value = Integer.parseInt(group, 16);
                    char ch = (char) value;
                    output += ch;    
                    group = "";
                }                
            }
            else{
                output += " ";
            }
        }
        return output;
    }
    
    public String hexToBin(String str){
        String input = str;
        clear();
        
        for (int i = 0, n = input.length(); i < n; i++) {
            char c = input.charAt(i);
            
            if(c != ' '){
                group += c;
            }
            else{
                int num = (Integer.parseInt(group, 16));
                output += Integer.toBinaryString(num) + " ";
                group = "";
            }
        }
        int num = (Integer.parseInt(group, 16));
        output += Integer.toBinaryString(num) + " ";
        group = "";
        
        return output.trim();
    }
    
    public String binToHex(String str){
        String input = str;
        clear();
        
         for (int i = 0, n = input.length(); i < n; i++) {
            char c = input.charAt(i);
            
            if(c != ' '){
                group += c;                                   // Should rename group
            }
            else{
                int decimal = Integer.parseInt(group, 2);
                output += Integer.toString(decimal,16) + " ";
                group = "";    
            }
        }
         int decimal = Integer.parseInt(group, 2);
         output += Integer.toString(decimal,16);
         
         return output;
    }
    
    public String binToDec(String str){
        String input = str;
        clear();
        
        for (int i = 0, n = input.length(); i < n; i++) {
            char c = input.charAt(i);
            if(c != ' '){
                group += c;
            }
            else{
                output += String.valueOf(Integer.parseInt(group, 2)) + " ";
                group = "";
            }
        }
        output += String.valueOf(Integer.parseInt(group, 2));
        group = "";
        
        return output;
    }
    
    public String decToBin(String str){
        String input = str;
        clear();
        
        for (int i = 0, n = input.length(); i < n; i++) {
            char c = input.charAt(i);
            if(c != ' '){
                group += c;
            }
            else{
                output += Integer.toBinaryString(Integer.parseInt(group)) + " ";
                group = "";
            }
        }
        output += Integer.toBinaryString(Integer.parseInt(group));
        group = "";
        
        return output;
    }
    
    public String hexToDec(String str){
        String input = str;
        clear();
        String digits = "0123456789ABCDEF";
        int val = 0;
        
        for (int i = 0; i < input.length(); i++){
            char c = input.charAt(i);
            int d = digits.indexOf(c);
            
            if(c != ' '){
                val = 16 * val + d; 
            }
            else{
                output += String.valueOf(val) + " ";
                val = 0;
            }
        }
        output += String.valueOf(val);
        val = 0;
        
        return output;
    }
    
    public String decToHex(String str){
        String input = str;
        clear();
        
        for (int i = 0, n = input.length(); i < n; i++) {
            char c = input.charAt(i);
            if(c != ' '){
                group += c;
            }
            else{
                output += Integer.toHexString(Integer.parseInt(group)) + " ";
                group = "";
            }
        }
        output += Integer.toHexString(Integer.parseInt(group));
        group = "";
        
        return output;
    }
    
    public String decimalToLetters(String str){
        clear();                                                // call clear method to make sure all variables are empty
        String input = str;
        String allNumbers = "";                              // string to display the decimals all at the bottom together
        char[] charArray = input.toCharArray();
        
        for (char c : charArray){
            if(c != ' '){
                for (int i = 0; i < alphabet.length; i++){
                    if (c == alphabet[i]){
                        output += (c + " : " + (i+1) + "\n");
                        allNumbers += (i + 1) + " "; 
                    }
                }
            }
            else{
                output += "\r\n\r\n";
            }
        }
        
        return output + "\r\n\r\n" + allNumbers;            // added the decimal numbers to be printed at bottom to copy paste for shifting
    }
    
    public String decimalToLettersShort(String str){
        clear();                                                // call clear method to make sure all variables are empty
        String input = str;
        String allNumbers = "";                              // string to display the decimals all at the bottom together
        char[] charArray = input.toCharArray();
        int num = 0;
        
        for (char c : charArray){
            if(c != ' '){
                allNumbers += c;
            }
            else{
                num = Integer.parseInt(allNumbers);
                output += alphabet[num - 1];
                num = 0;
                allNumbers = "";
            }
        }
        
        num = Integer.parseInt(allNumbers);
        output += alphabet[num - 1];
        num = 0;
        allNumbers = "";
        
        return output;            // added the decimal numbers to be printed at bottom to copy paste for shifting
    }
    
    public String lettersToDecimal(String str){
        clear();
        String input = str;
        char[] charArray = input.toCharArray();
        
        
        
        for (char c : charArray){
            if( c != ' '){
                for(int i = 0; i < alphabet.length; i++){
                    if( c == alphabet[i]){
                        output += (i + 1) + " ";
                    }
                }
            }
            else{
                output += "";
            }
        }
        
        return output.trim();
    }
    
}
