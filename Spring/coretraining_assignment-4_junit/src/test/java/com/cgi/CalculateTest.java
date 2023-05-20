package com.cgi;

/* Name: Deepak Kumar Mandal
 * Email: dkm.iit.g@gmail.com
 * 
 * 1) Create a class Calculate Create a method int addSum(int a, int b);
 *  boolean isEven(int num);*/

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class CalculateTest {
	
	//Creating object
	Calculate c=new Calculate();
	
	//Prameterized Testcases using Junit addSum() method
	@Test
	void testAddSum() {
		assertEquals(20, c.addSum(5, 15));		//positive scenario
	}
	
	@Test
	void testAddSum2() {
		assertNotEquals(11, c.addSum(1, 1));		//negative scenario
	}
	
	//Prameterized Testcases using Junit isEven() method
	@Test
	void testIsEven1() {
		assertTrue(c.isEven(18));		//+ve scenario
	}
	
	@Test 
	void testIsEven2(){
		assertFalse(c.isEven(3));		////-ve scenario
	}
	
	
}
