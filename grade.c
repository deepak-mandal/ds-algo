#include <stdio.h>
int main()
{
float s11, s12, s13, s14, s15, s16, s17, s21, s22, s23, s24, s25, s26, s27, s28, s31, s32, s33, s34, s35, s36, s41, s42, s43, s44, s45, s46, s51, s52, s53, s54, s55, s56;
float s61, s62, s63, s64, s65, s66, s71, s72, s73, s74, s75, s76, s81, s82, s83, s84, s85;
float spi1, spi2, spi3, spi4, spi5, spi6, spi7, spi8, cpi1, cpi2, cpi3, cpi4, cpi5, cpi6, cpi7, cpi8, x1, y1; 

printf("\n");
/*
AA = 10;
AB = 9;
BB = 8;
BC = 7;
CC = 6;
CD = 5;
DD = 4;
*/

//S1
s11 = 6;	//Chemistry
s12 = 8;	//Chemistry Laboratory
s13 = 4;	//Electrical Science
s14 = 6;	//Mathematics-1
s15 = 7;	//Engineering drawing
s16 = 4;	//Physics-1
s17 = 6;	//Physics Laboratory

spi1 = (8*s11+3*s12+8*s13+8*s14+5*s15+6*s16+3*s17)/(8+3+8+8+5+6+3);
x1 = (8*s11+3*s12+8*s13+8*s14+5*s15+6*s16+3*s17);
y1 = (8+3+8+8+5+6+3);
cpi1 = (x1)/(y1);

printf("SPI_1 = %f\n", spi1);
printf("CPI_1 = %f\n", cpi1);
printf("\n");

//S2
s21 = 6;	//Modern Biology
s22 = 4;	//Introduction to computing
s23 = 6;	//Computational Laboratory
s24 = 8;	//Basic Electronics Laboratory
s25 = 4;	//Mathematis-2
s26 = 4;	//Engineering Mechanics
s27 = 9;	//Mechanical Workshop
s28 = 8;	//Physics-2

spi2 = (6*s21+6*s22+3*s23+3*s24+8*s25+8*s26+3*s27+6*s28)/(6+6+3+3+8+8+3+6);
x1 = x1 + (6*s21+6*s22+3*s23+3*s24+8*s25+8*s26+3*s27+6*s28);
y1 = y1 + (6+6+3+3+8+8+3+6);
cpi2 = (x1)/(y1);

printf("SPI_2 = %f\n", spi2);
printf("CPI_2 = %f\n", cpi2);
printf("\n");

//S3
s31 = 7;	//Organic Chemistry
s32 = 5;	//Introduction to Quantum Chemistry
s33 = 4;	//Chemical Process Calculations
s34 = 6;	//Fluid Mechanics
s35 = 5;	//Introduction to Phonetics
s36 = 4;	//Mathematics-3
	
spi3 = (8*s31+6*s32+6*s33+8*s34+6*s35+8*s36)/(8+6+6+8+6+8);
x1 = x1 + (8*s31+6*s32+6*s33+8*s34+6*s35+8*s36);
y1 = y1 + (8+6+6+8+6+8);
cpi3 = (x1)/(y1);

printf("SPI_3 = %f\n", spi3);
printf("CPI_3 = %f\n", cpi3);
printf("\n");

//S4
s41 = 7;	//Inorganic Chemistry
s42 = 6;	//Applied Organic Chemistry
s43 = 9;	//Chemical Technology Labouratory-1
s44 = 5;	//Computational Chemistry
s45 = 5;	//Spectroscopic Technique in Chemistry
s46 = 7;	//Socialogy of India : Conformities and Contradictions

spi4 = (6*s41+6*s42+6*s43+8*s44+6*s45+6*s46)/(6+6+6+8+6+6);
x1 = x1 + (6*s41+6*s42+6*s43+8*s44+6*s45+6*s46);
y1 = y1 + (6+6+6+8+6+6);
cpi4 = (x1)/(y1);

printf("SPI_4 = %f\n", spi4);
printf("CPI_4 = %f\n", cpi4);
printf("\n");

//S5
s51 = 8; 	//Environmental Chemistry
s52 = 9;	//Industrial Chemistry
s53 = 10;	//Chemical Technology Labouratory-2
s54 = 8;	//Chemical Kinetics and Electrochemistry
s55 = 8;	//Social History of Technology in modern India
s56 = 7;	//Computational Physics
	
spi5 = (6*s51+6*s52+6*s53+6*s54+6*s55+6*s56)/(6+6+6+6+6+6);
x1 = x1 + (6*s51+6*s52+6*s53+6*s54+6*s55+6*s56);
y1 = y1 + (6+6+6+6+6+6);
cpi5 = (x1)/(y1);

printf("SPI_5 = %f\n", spi5);
printf("CPI_5 = %f\n", cpi5);
printf("\n");

/*                                                     Hypothesis only (not_in_Real) to Analyse data of upcoming result 									*/
printf("\nHypothesis only (not_in_Real) to Analyse data of upcoming result [Let SPI_9]\n");
//S6
s61 = 9; 
s62 = 9;
s63 = 9;
s64 = 9;
s65 = 9;
s66 = 9;

spi6 = (8*s61+6*s62+6*s63+6*s64+6*s65+6*s66)/(8+6+6+6+6+6);
x1 = x1 + (8*s61+6*s62+6*s63+6*s64+6*s65+6*s66);
y1 = y1 + (8+6+6+6+6+6);
cpi6 = (x1)/(y1);

printf("SPI_6 = %f\n", spi6);
printf("CPI_6 = %f\n", cpi6);
printf("\n");

//S7
s71 = 9;
s72 = 9;
s73 = 9;
s74 = 9;
s75 = 9;
s76 = 9;
 
spi7 = (6*s71+3*s72+6*s73+6*s74+6*s75+6*s76)/(6+3+6+6+6+6);
x1 = x1 + (6*s71+3*s72+6*s73+6*s74+6*s75+6*s76);
y1 = y1 + (6+3+6+6+6+6);
cpi7 = (x1)/(y1);

printf("SPI_7 = %f\n", spi7);
printf("CPI_7 = %f\n", cpi7);
printf("\n");

//S8
s81 = 9;
s82 = 9;
s83 = 9;
s84 = 9;
s85 = 9;

spi8 = (6*s81+6*s82+6*s83+6*s84+6*s85)/(6+6+6+6+6);
x1 = x1 + (6*s81+6*s82+6*s83+6*s84+6*s85);
y1 = y1 + (6+6+6+6+6);
cpi8 = (x1)/(y1);

printf("SPI_8 = %f\n", spi8);
printf("CPI_8 = %f\n", cpi8);
printf("\n");

return 0;
}
