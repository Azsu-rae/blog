#! /bin/bash

psql service=admin --command="DROP DATABASE IF EXISTS blog;"
psql service=admin --command="CREATE DATABASE blog;"
