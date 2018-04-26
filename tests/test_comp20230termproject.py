#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `xinyuewang` package."""

import unittest
from click.testing import CliRunner
import cli
from xinyuewang.Aircraft import Aircraft
from xinyuewang.cost import distanceBlackBox
from xinyuewang.AirportAtlas import AirportAtlas
from xinyuewang.Airport import Airport

class TestComp20230termproject(unittest.TestCase):
    """Tests for `xinyuewang` package."""
    #test instance for all
    route = ['OLA', 'MNZ', 'OLT', 'ELU', 'EGR']
    ac = Aircraft()
    ac.loadData()
    aa = AirportAtlas()
    aa.loadData()

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main,['-i input/testInput2.csv'])
        assert result.exit_code == 0
        assert " " in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert "--help     Show this message and exit." in help_result.output
        assert "-i TEXT    Input file for route calculation." in help_result.output
        #self.assertIsInstance(disDict, set)
        
    #Too lazy to write loadData test for each, make a common function to call
    def loadData(self,ists):
        with self.assertRaises(IOError):
            ists.loadData('whatever')
            
    def test_Aircraft(self):
        '''test for aircraft class'''
        self.loadData(self.ac)
        #with self.assertRaises(IOError):
        #    self.ac.loadData('whatever')
        self.assertIsInstance(self.ac.getCrafts(), dict)
        assert self.ac.getCrafts()
        assert self.ac.getRange('A319') == 3750
        assert self.ac.getRange('777') == 9700*1.60934
        with self.assertRaises(KeyError):
            self.ac.getRange('code')
        assert 'BAE146' in self.ac.planeSet()
    
    def test_Airport(self):
        ap = Airport('DUB','Dublin','Ireland',0.4,1)
        self.assertIsInstance(ap, Airport)
        assert ap.code == 'DUB'
        self.assertEqual('Dublin', ap.name)
        
    def test_AirportAtlas(self):
        self.assertIsInstance(self.aa,AirportAtlas)
        self.loadData(self.aa)
        self.assertIsInstance(self.aa.getAtlas(),dict)
        self.assertIn('DUB', self.aa.getAtlas())
        assert 'LUP' in self.aa.getAtlas()
        self.assertIsInstance(self.aa.getAirport('DUB'),Airport)
        with self.assertRaises(KeyError):
            self.aa.getAirport('imadethisup')
        
        #LHR - DEN
        self.assertAlmostEqual(self.aa.greatCircleDist(51.470020, -0.454295,39.849312, -104.673828),  7496.11,delta=5)
        self.assertAlmostEqual(self.aa.getDistanceBetweenAirports('LHR','DEN'),7496.11,delta=5)
        self.assertIsInstance(self.aa.getAirportByName('Dublin'), Airport)
    
    # So, I need to initial the graph with different distances, if the distance is 
    # out of range, the two nodes will not be linked...
    def test_distanceBlackbox(self):
        assert distanceBlackBox('777',self.route,self.ac,self.aa) 
    
    

        
    
