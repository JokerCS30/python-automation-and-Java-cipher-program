/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package shiftingandconverting;

import java.util.ArrayList;
import java.util.Random;

/**
 *
 * @author Jamie
 */
public class Ceasar {
    
    String alphabetString = "abcdefghijklmnopqrstuvwxyz";
    char[] alphabet = alphabetString.toCharArray();             // create a character array of the alphabet
    conversions convert =  new conversions();
    String input = "";
    String output = "";
    
    private void clear(){
        input = "";
        output = "";
    }
    
    public String rotateSingle(int num, String str){            // rotate input by the same number
        int rotationNumber = num;
        String string = str.toLowerCase();
        char[] charArray = string.toCharArray();        // convert the string to an array with chars
        String shifted = "";
        
        clear();
        
        for (char c : charArray){
            
            if (c != ' '){                
                for (int i = 0; i < alphabet.length; i++){
                    if (c == alphabet[i]){
                        int x = i + num;
                        if(x < 26){
                            shifted += alphabet[x];               // this assigns the shifted letter to the string
                        }
                        else{
                            x = x - 26;
                            shifted += alphabet[x];              // subtracts 26 eg z + 1 becomes a
                        }
                    }
                }               
            }
            else{
                shifted += " ";
            }
        }
        
        return shifted;
    }
    
    public String rotateWord(String wordInput, String textInput){           // rotate the input by a rotation word
        String rotationWord = wordInput.toLowerCase();                                    // the rotation word
        input = textInput.toLowerCase();                                   // the input which will be rotated
        char[] wordArray = rotationWord.toCharArray();                      // character array from the rotation word
        char[] charArray = input.toCharArray();                     // character array from the input that is to be rotated
        ArrayList<Integer> pattern = new ArrayList<Integer>();      // an arrayList which will hold the indexed number of letters
        int counter = 0;
        
        clear();
        
        for(char c : wordArray){                                    // for each character in the rotation word
            for(int i = 0; i < alphabet.length; i++){
                if(c == alphabet[i]){                               // when the character matches its corresponding in alphabet array
                    pattern.add(i + 1);                             // add its index of alphabet plus one as index starts at 0
                }
            }
        }
        
        
        for(char c : charArray){                                    // for each letter of our input
           if (c != ' '){                                           // if not a space
                output += rotateSingle(pattern.get(counter), String.valueOf(c));        // rotate a leter at a time from rotation word hence counter
                counter++;                                                              // counter increments so next letter of rotation word will be used
           }
           else{
               output += " ";
           }
           
           if (counter == pattern.size()){              // to reset the counter once the pattern has been used once
               counter = 0;
           }
        }
       
        return output;        
    }
    
    public String reverseWord(String input){            // this method is to revers a words indexing of the alphabet in order to cipher string as the normal word would decipher it
        String word = input.toLowerCase();
        char[] wordArray = word.toCharArray();          // creates a character array of all characters from the rotation word
        String stringNumber = "";
        
        clear();
        
        for(char c : wordArray){                                    // for each character in the rotation word
            if(c != ' '){
                for(int i = 0; i < alphabet.length; i++){
                    if(c == alphabet[i]){                               // when the character matches its corresponding in alphabet array
                        stringNumber += (26 - (i + 1)) + " ";
                    }
                }
            }
            else{
                
            }
        }
        output = convert.decimalToLettersShort(stringNumber.trim());
        
        return output;
    }
    
    public String scramble(String input){
        clear();
        this.input = input.toLowerCase();
        Random r = new Random();
        
        
        // Convert your string into a simple char array:
        char a[] = input.toCharArray();

        // Scramble the letters using the standard Fisher-Yates shuffle, 
        for( int i=0 ; i<a.length-1 ; i++ )
        {
            int j = r.nextInt(a.length-1);
            // Swap letters
            char temp = a[i]; a[i] = a[j];  a[j] = temp;
        }       

        return new String( a );
        }
    
    public String checkDictionary(String input){
        clear();
        this.input = input;
        ArrayList<String> allWords = new ArrayList<>();                         // this arraylist will host all the scrambled words to then be able to methodically check each in a dictionary
        
        
        for(String s : input.split(" ")){
            allWords.add(s);
        }
        
        
        
        for(int i = 0; i < allWords.size(); i++){
            
            if (allWords.get(i).equalsIgnoreCase("everything")){
                output = "contains word everything";
            }
            else if(output == ""){
                output = "doesn't contain word everything";
            }
        }
        
        return output;
    }
    
    public String count(String input){
        clear();
        this.input = input;
        ArrayList<String> words = new ArrayList<>();
        char[] array = input.toCharArray();
        int letterCount = 0;
        int wordCount = 0;
        
        if(!(input.isEmpty())){
            for(String s : input.split(" ")){
                words.add(s);
            }

            for(char c : array){
                if(c != ' '){
                    letterCount++;
                }
            }
        }
            
        return("Words = " + words.size() + "    Letters = " + letterCount);
        
    }
}
 