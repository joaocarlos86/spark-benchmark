# Spark CPU benchmark

## Overview

This is the first part of the benchmark, the code stress the CPU by running several Spark tasks to calculate a series of numbers (a ** b). This code is targeted to run inside a CPU.

## Instalation

docker build -t spark .

## Usage

docker run --rm --name myspark spark
