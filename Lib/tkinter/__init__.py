import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt

class RiskAssessment:
    def __init__(self):
        self.risks = []

    def add_risk(self, risk_type, description, probability, severity, frequency, control_measures, employee_feedback):
        risk_score = probability * severity * frequency
        self.risks.append({
            "Risk Type": risk_type,
            "Description": description,
            "Probability": probability,
            "Severity": severity,
            "Frequency": frequency,
            "Risk Score": risk_score,
            "Control Measures": control_measures,
            "Employee Feedback": employee_feedback
        })
    
    def generate_report(self):
        df = pd.DataFrame(self.risks)
        df = df.sort_values(by="Risk Score", ascending=False)
        return df
    
    def export_to_excel(self, filename):
        df = self.generate_report()
        df.to_excel(filename, index=False)
    
    def generate_chart(self):
        df = self.generate_report()
        if df.empty:
            messagebox.showinfo("Info", "No data available to generate chart.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.bar(df["Risk Type"], df["Risk Score"], color='red')
        plt.xlabel("Risk Type")
        plt.ylabel("Risk Score")
        plt.title("Risk Assessment Chart")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

# GUI Implementation
def submit_risk():
    risk_type = entry_risk_type.get()
    description = entry_description.get()
    probability = int(entry_probability.get())
    severity = int(entry_severity.get())
    frequency = int(entry_frequency.get())
    control_measures = entry_control_measures.get()
    employee_feedback = entry_employee_feedback.get()
    
    assessment.add_risk(risk_type, description, probability, severity, frequency, control_measures, employee_feedback)
    messagebox.showinfo("Success", "Risk added successfully!")

def export_report():
    filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if filename:
        assessment.export_to_excel(filename)
        messagebox.showinfo("Success", "Report exported successfully!")

def show_chart():
    assessment.generate_chart()

assessment = RiskAssessment()

root = tk.Tk()
root.title("Risk Assessment Tool")

tk.Label(root, text="Risk Type:").pack()
entry_risk_type = tk.Entry(root)
entry_risk_type.pack()

tk.Label(root, text="Description:").pack()
entry_description = tk.Entry(root)
entry_description.pack()

tk.Label(root, text="Probability (1-5):").pack()
entry_probability = tk.Entry(root)
entry_probability.pack()

tk.Label(root, text="Severity (1-5):").pack()
entry_severity = tk.Entry(root)
entry_severity.pack()

tk.Label(root, text="Frequency (1-5):").pack()
entry_frequency = tk.Entry(root)
entry_frequency.pack()

tk.Label(root, text="Control Measures:").pack()
entry_control_measures = tk.Entry(root)
entry_control_measures.pack()

tk.Label(root, text="Employee Feedback:").pack()
entry_employee_feedback = tk.Entry(root)
entry_employee_feedback.pack()

tk.Button(root, text="Add Risk", command=submit_risk).pack()
tk.Button(root, text="Export Report", command=export_report).pack()
tk.Button(root, text="Show Chart", command=show_chart).pack()

root.mainloop()
