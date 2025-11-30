# Cycle Calculator Tool: Calculates cycle phase and predicts next period

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime, timedelta
from setup import FunctionTool

def calculate_cycle_phase(last_period_date: str, cycle_length: int = 28) -> dict:
    """
    Calculate the current cycle phase based on last period date.
    
    Args:
        last_period_date: Date of last period in format 'YYYY-MM-DD'
        cycle_length: Average cycle length in days (default: 28)
    
    Returns:
        Dictionary with cycle phase, days since period, and next period prediction
    """
    try:
        # Parse the date
        last_period = datetime.strptime(last_period_date, "%Y-%m-%d")
        today = datetime.now()
        
        # Calculate days since last period
        days_since_period = (today - last_period).days
        
        # Calculate day in current cycle (handle cases where period is overdue)
        day_in_cycle = days_since_period % cycle_length
        
        # Determine cycle phase based on day in cycle
        # Menstrual: Days 1-5
        # Follicular: Days 6-13
        # Ovulation: Days 14-16
        # Luteal: Days 17-28
        
        if day_in_cycle <= 5:
            phase = "Menstrual"
            phase_description = "Your period is here. Focus on rest and gentle self-care."
        elif day_in_cycle <= 13:
            phase = "Follicular"
            phase_description = "Energy is rising! Good time for new projects and social activities."
        elif day_in_cycle <= 16:
            phase = "Ovulation"
            phase_description = "Peak energy and confidence. Great for important conversations and challenges."
        else:
            phase = "Luteal"
            phase_description = "Energy may dip. Prioritize rest, boundaries, and comfort."
        
        # Calculate next period date
        next_period = last_period + timedelta(days=cycle_length)
        days_until_period = (next_period - today).days
        
        return {
            "current_phase": phase,
            "phase_description": phase_description,
            "day_in_cycle": day_in_cycle,
            "days_since_last_period": days_since_period,
            "next_period_date": next_period.strftime("%Y-%m-%d"),
            "days_until_next_period": days_until_period,
            "cycle_length": cycle_length
        }
        
    except ValueError as e:
        return {
            "error": f"Invalid date format. Please use YYYY-MM-DD format. Error: {str(e)}"
        }
    except Exception as e:
        return {
            "error": f"Error calculating cycle phase: {str(e)}"
        }

# Test the function
print("✅ Cycle calculator function created")
print(f"Test: {calculate_cycle_phase('2025-11-23', 28)}")  # Using Nov 25, 2025 as test date

# Create the FunctionTool
cycle_calculator_tool = FunctionTool(
    func=calculate_cycle_phase
)

print("✅ cycle_calculator_tool wrapped as FunctionTool")