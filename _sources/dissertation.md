# Dissertation Research

## Pricing Asian Options using Monte Carlo Simulation

This dissertation investigates numerical techniques for pricing path-dependent derivatives, focusing on the application of Monte Carlo simulation methods to arithmetic Asian options.

Asian options are derivatives whose payoff depends on the average price of the underlying asset over time, making them path-dependent and more complex to price than standard European options.

Because arithmetic Asian options typically do not admit closed-form analytical solutions, Monte Carlo simulation provides a natural framework for estimating their expected payoff under risk-neutral dynamics.

## Research Objective

The objective of this research is to analyse the convergence and numerical behaviour of Monte Carlo estimators when applied to pricing arithmetic Asian options under a Geometric Brownian Motion model.

The project focuses particularly on:

- statistical convergence of Monte Carlo estimators
- discretisation error arising from time-stepping schemes
- computational efficiency of simulation methods
- variance reduction techniques

## Theoretical Framework

The dissertation draws on several core concepts from mathematical finance:

- the no-arbitrage principle
- risk-neutral pricing
- stochastic modelling of asset prices
- Brownian motion and stochastic differential equations

In continuous-time financial models, asset prices are typically modelled as stochastic processes driven by Brownian motion.

## Numerical Analysis

The research investigates several important sources of numerical error:

- sampling error from finite simulations
- discretisation bias in time-stepping schemes
- modelling assumptions such as the Geometric Brownian Motion framework

Variance reduction techniques such as antithetic variates and control variates are explored in order to improve simulation efficiency.

The broader goal is to understand how numerical simulation methods can be applied to solve complex pricing problems where analytical solutions are unavailable.

