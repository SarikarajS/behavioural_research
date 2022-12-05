#include <iostream>
#include <fstream>   
#include <string>    
#include <list> 
#include <ctime>
#include <cstdlib>
#include <vector>

using namespace std;

int main()
{
    srand((unsigned)time(NULL));

    int MIN_VALUE = 0;
    int MAX_VALUE = 9;

    std::vector<int> multiplyAllNumsList1;

    //fill array with 20 values
    for (int i = 2; i < (22); i++) {
        multiplyAllNumsList1.push_back(i);
    }

    // shuffle the array
    for (int i = 0; i < multiplyAllNumsList1.size(); i++) {
        int randomIndex = rand() % multiplyAllNumsList1.size();
        int temp = multiplyAllNumsList1[i];

        multiplyAllNumsList1[i] = multiplyAllNumsList1[randomIndex];
        multiplyAllNumsList1[randomIndex] = temp;
    }

    // shuffle twice for luck ^_^
    for (int i = 0; i < multiplyAllNumsList1.size(); i++) {
        int randomIndex = rand() % multiplyAllNumsList1.size();
        int temp = multiplyAllNumsList1[i];

        multiplyAllNumsList1[i] = multiplyAllNumsList1[randomIndex];
        multiplyAllNumsList1[randomIndex] = temp;
    }

    std::vector<int> multiplyAllNumsList2 = multiplyAllNumsList1;
    std::vector<int> multiplyAllNumsList3 = multiplyAllNumsList1;
    std::vector<int> multiplyAllNumsList4 = multiplyAllNumsList1;

    // add and subtract numbs
    std::vector<int> numList1AllNums;
    std::vector<int> numList2AllNums;

    // loop for the number of files that are required 
    for (int fileCount = 0; fileCount < 5; fileCount++) {

        //create two arrays representing two columns of numbers
        std::vector<int> numList1;
        std::vector<int> numList2;
        int numList = 2;

        for (int listCount = 1; listCount < 3; listCount++) {

            for (int validNumbers = 1; validNumbers <= 4;) {
                // create random tens from 0 to 5
                int randomTensNumber = rand() % (5 - 0 + 1);

                if (randomTensNumber == 0) {
                    randomTensNumber = 1;
                }

                int randomNumber = (randomTensNumber * 10) + (rand() % (MAX_VALUE - MIN_VALUE + 1));
                bool numOriginal = true;

                switch (listCount) {
                case 1:
                    // check in the new number is already in list 1 all numbers list
                    for (int listPos = 0; listPos < numList1AllNums.size(); listPos++) {
                        if (numList1AllNums[listPos] == randomNumber) {
                            numOriginal = false;
                        }
                    }
                    if (numOriginal == true) {
                        // check in the new number is already in list 2
                        for (int listPos = 0; listPos < numList2AllNums.size(); listPos++) {

                            if (numList2AllNums[listPos] == randomNumber) {
                                numOriginal = false;
                            }
                        }
                    }
                    // if the new number is not in list1 it gets added to list1
                    if (numOriginal == true) {
                        numList1.push_back(randomNumber);
                        numList1AllNums.push_back(randomNumber);
                        validNumbers++;
                    }
                    break;
                case 2:
                    // check in the new number is already in list 1 all numbs
                    for (int listPos = 0; listPos < numList1AllNums.size(); listPos++) {

                        if (numList1AllNums[listPos] == randomNumber) {
                            numOriginal = false;
                        }
                    }

                    if (numOriginal == true) {
                        // check in the new number is already in list 2
                        for (int listPos = 0; listPos < numList2AllNums.size(); listPos++) {

                            if (numList2AllNums[listPos] == randomNumber) {
                                numOriginal = false;
                            }
                        }
                    }

                    // if the new number is not in either list it gets added to list two
                    if (numOriginal == true == true) {
                        numList2.push_back(randomNumber);
                        numList2AllNums.push_back(randomNumber);
                        validNumbers++;
                    }
                    break;
                }
            }
        }

        // create add subtract numbers 
        std::vector<int> column1List;
        std::vector<int> column2List;

        int startingColumn2 = numList2[0];
        bool loopComplete = false;

        while (!loopComplete) {

            for (int listPos = 0; listPos < numList1.size(); listPos++) {
                // push back the first number in the first list
                column1List.push_back(numList1[listPos]);
                // push back the first number in the second list
                column2List.push_back(numList2[listPos]);
            }

            // take the number at the start of list 2
            int numToMove = numList2[0];
            // then delete it from the frount of the list
            numList2.erase(numList2.begin());
            //insert it back into the list at the back
            numList2.push_back(numToMove);

            // if both numbers are the same as they where at the start we have done all the combinations we can
            if (numList2[0] == startingColumn2) {
                loopComplete = true;
            }
        }

        std::vector<int> column1ListTemp = column1List;

        for (int i = 0; i < (column2List.size() - 1); i++) {
            // push back the first number in the first list
            column1List.push_back(column2List[i]);
        }

        for (int i = 0; i < (column1ListTemp.size() - 1); i++) {
            // push back the first number in the second list
            column2List.push_back(column1ListTemp[i]);
        }

        // create mutiplication questions
        std::vector<int> column1multiplicationList;
        std::vector<int> column2multiplicationList;

        for (int timesTableNum = 0; timesTableNum < 3; timesTableNum++) {
            switch (timesTableNum) {
            case 0:
                // 10 times table
                for (int i = 1; i < 5; i++) {
                    column1multiplicationList.push_back(10);
                    //load the first num in the array in to newMultiplyNum 
                    int newMultiplyNum = multiplyAllNumsList1[0];
                    //Then erase that number
                    multiplyAllNumsList1.erase(multiplyAllNumsList1.begin());
                    // add it to the list
                    column2multiplicationList.push_back(newMultiplyNum);
                }
                break;
            case 1:
                // 5 times table
                for (int i = 1; i < 5; i++) {
                    column1multiplicationList.push_back(5);
                    //load the first num in the array in to newMultiplyNum 
                    int newMultiplyNum = multiplyAllNumsList2[0];
                    //Then erase that number
                    multiplyAllNumsList2.erase(multiplyAllNumsList2.begin());
                    // add it to the list
                    column2multiplicationList.push_back(newMultiplyNum);
                }
                break;
            case 2:
                // 2 times table
                for (int i = 1; i < 5; i++) {
                    column1multiplicationList.push_back(2);
                    //load the first num in the array in to newMultiplyNum 
                    int newMultiplyNum = multiplyAllNumsList4[0];
                    //Then erase that number
                    multiplyAllNumsList4.erase(multiplyAllNumsList4.begin());
                    // add it to the list
                    column2multiplicationList.push_back(newMultiplyNum);
                }
                break;
            }

            std::vector<int> column1multiplicationListTemp = column1multiplicationList;

            for (int i = 0; i < column2multiplicationList.size(); i++) {
                column1multiplicationList.push_back(column2multiplicationList[i]);
            }

            for (int i = 0; i < column1multiplicationListTemp.size(); i++) {
                column2multiplicationList.push_back(column1multiplicationListTemp[i]);
            }

            fstream file;

            switch (fileCount) {
            case 0:
                //opening an existing csv file or creating a new csv file if there is not an existing one 
                file.open("mathQuestionsA.csv", ios::out);
                break;
            case 1:
                file.open("mathQuestionsB.csv", ios::out);
                break;
            case 2:
                file.open("mathQuestionsC.csv", ios::out);
                break;

            case 3:
                file.open("mathQuestionsD.csv", ios::out);
                break;
            case 4:
                file.open("mathQuestionsE.csv", ios::out);
                break;
            }

           // inserting headers 
            file << "CategoryType" << "," << "NumOne" << "," << "NumTwo" << "," <<
                "Correct" << "," << "Incorrect1" << "," << "Incorrect2" << "," << "Incorrect3" << "\n";

            int MIN_Offset_VALUE = -5;
            int MAX_Offset_VALUE = 5;

            // add addition questions
            for (int i = 0; i < column1List.size(); i++) {

                int correctAwanserInt = column1List[i] + column2List[i];

                int offset1 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset1 == 0) {
                    offset1 = 10;
                }
               
                int offset2 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset2 == 0) {
                    offset2 = 10;
                }

                if (offset2 == offset1) {
                    offset2 += 2;
                }


                int offset3 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset3 == 0) {
                    offset3 = 10;
                }

                if (offset3 == offset2) {
                    offset3 += 4;
                }

                // addition  
                file << "add" << "," << column1List[i] << "," << column2List[i] << "," <<
                    correctAwanserInt << "," << correctAwanserInt + offset1 << "," << correctAwanserInt + offset2 << "," << correctAwanserInt + offset3 << "\n";
            }


            // add subtraction questions
            for (int i = 0; i < column1List.size(); i++) {
               
                // Eliminate negative awansers 
                if ((column1List[i] - column2List[i]) < 0) {
                    column1List[i] += (((column1List[i] - column2List[i]) * -1) + (rand() % (15 - 10 + 1)));
                }

                int correctAwanserInt = column1List[i] - column2List[i];

                int offset1 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset1 == 0) {
                    offset1 = -10;                
                }

                // Eliminate negative wrong awansers 
                if ((correctAwanserInt + offset1) < 0) {
                    offset1 = offset1 + rand() % (9 - 12 + 1);
                }
                // insure that the wrong awanser cant be equal to the correct awanser
                if (offset1 == correctAwanserInt) {
                    offset1++;
                }


                int offset2 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset2 == 0) {
                    offset2 = -10;
                }
                // Eliminate negative awansers 
                if ((correctAwanserInt + offset2) < 0) {
                    offset2 = correctAwanserInt + rand() % (5 - 8 + 1);
                }
                if (offset2 == offset1) {
                    offset2 += 2;
                }
                // insure that the wrong awanser cant be equal to the correct awanser
                if (offset2 == correctAwanserInt) {
                    offset2++;
                }
                int offset3 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset3 == 0) {
                    offset3 = -10;
                }
                // Eliminate negative awansers 
                if ((correctAwanserInt + offset3) < 0) {
                    offset3 = correctAwanserInt + rand() % (1 - 4 + 1);
                }
                if (offset3 == offset2) {
                    offset3 += 4;
                }
                // insure that the wrong awanser cant be equal to the correct awanser
                if (offset3 == correctAwanserInt) {
                    offset3++;
                }
                // subtraction  
                file << "subtract" << "," << column1List[i] << "," << column2List[i] << "," <<
                    correctAwanserInt << "," << correctAwanserInt + offset1 << "," << correctAwanserInt + offset2 << "," << correctAwanserInt + offset3 << "\n";
            }


            // add multiply questions
            for (int i = 0; i < column1multiplicationList.size(); i++) {

                int correctAwanserInt = column1multiplicationList[i] * column2multiplicationList[i];

                int offset1 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset1 == 0) {
                    offset1 = 10;
                }

                // Eliminate negative awansers 
                if ((correctAwanserInt + offset1) < 0) {
                    offset1 = correctAwanserInt + rand() % (9 - 12 + 1);
                }
                int offset2 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset2 == 0) {
                    offset2 = 10;
                }

                // Eliminate negative awansers 
                if ((correctAwanserInt + offset2) < 0) {
                    offset2 = correctAwanserInt + rand() % (5 - 8 + 1);
                }

                if (offset2 == offset1) {
                    offset2 += 2;
                }

                int offset3 = rand() % (MIN_Offset_VALUE - MAX_Offset_VALUE + 1);
                if (offset3 == 0) {
                    offset3 = 10;
                }

                // Eliminate negative awansers 
                if ((correctAwanserInt + offset3) < 0) {
                    offset3 = correctAwanserInt + rand() % (1 - 4 + 1);
                }

                if (offset3 == offset2) {
                    offset3 += 4;
                }


                // multiply  
                file << "multiply" << "," << column1multiplicationList[i] << "," << column2multiplicationList[i] << "," <<
                    correctAwanserInt << "," << correctAwanserInt + offset1 << "," << correctAwanserInt + offset2 << "," << correctAwanserInt + offset3 << "\n";
            }

            file.close();   // closing csv file
            fstream fin;
            string data;
        }
    }
    
    cout << "\n\n5 new CSV files have been successfully created and the new questions added!";
    cout << "\nI hope they are helpful^_^ \nbye bye now\n\n\n";

    return 0;

}