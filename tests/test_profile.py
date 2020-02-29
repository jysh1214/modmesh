# Copyright (c) 2019, Yung-Yu Chen <yyc@solvcon.net>
# BSD-style license; see COPYING


import unittest
import time

import modmesh


class StopWatchTC(unittest.TestCase):

    def test_singleton(self):

        self.assertIs(modmesh.stop_watch, modmesh.StopWatch.me)

    def test_microsecond_resolution(self):

        sw = modmesh.stop_watch
        self.assertGreater(1.e-6, sw.resolution)

    def test_lap_with_sleep(self):

        sw = modmesh.stop_watch

        # Mark start
        sw.lap()

        time.sleep(0.01)

        elapsed = sw.lap()
        self.assertGreater(elapsed, 0.01)
        # Don't test for the upper bound. CI doesn't like it (to be specific,
        # mac runner of github action).


class TimeRegistryTC(unittest.TestCase):

    def test_singleton(self):

        self.assertIs(modmesh.time_registry, modmesh.TimeRegistry.me)

    def test_empty_report(self):

        ret = modmesh.time_registry.report()
        self.assertEqual("", ret)

# vim: set ff=unix fenc=utf8 et sw=4 ts=4 sts=4:
