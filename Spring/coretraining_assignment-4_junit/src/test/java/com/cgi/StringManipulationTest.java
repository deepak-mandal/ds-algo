package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 2) Create a class StringManipulation and create a method 
 * int vowelCount(String name); int characterCount(String str);*/

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class StringManipulationTest {
	
	//creating object
	StringManipulation sm=new StringManipulation();

	//Prameterized Testcases using Junit vowelCount() method
	@Test
	void testVowelCount1() {
		assertEquals(3, sm.vowelCount("Deepak"));		//positive scenario
	}
	
	@Test
	void testVowelCount2() {
		assertNotEquals(5, sm.vowelCount("Kumar"));		//negative scenario
	}
	
	//Prameterized Testcases using Junit characterCount() method
	@Test
	void testcharacterCount1() {
		assertEquals(6, sm.characterCount("Deepak18101998"));		//positive scenario
	}
	
	@Test
	void testcharacterCount2() {
		assertNotEquals(14, sm.characterCount("Deepak18101998"));		//negative scenario
	}

}
