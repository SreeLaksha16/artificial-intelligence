% ======================================
% Simple Medical Diagnosis System
% ======================================

% ---------- Facts: Symptoms ----------
% symptom(Patient, Symptom)

% Example patients
% (for demonstration, you can query and add dynamically)
% symptom(john, fever).
% symptom(john, cough).

% ---------- Disease Rules ----------
% Define diseases based on symptoms

disease(flu, Patient) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, body_ache).

disease(cold, Patient) :-
    symptom(Patient, cough),
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose).

disease(covid19, Patient) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, loss_of_taste_smell),
    symptom(Patient, shortness_of_breath).

disease(malaria, Patient) :-
    symptom(Patient, fever),
    symptom(Patient, chills),
    symptom(Patient, sweating).

disease(allergy, Patient) :-
    symptom(Patient, sneezing),
    symptom(Patient, itchy_eyes),
    symptom(Patient, runny_nose).

% ---------- Diagnosis Rule ----------
% Find all possible diseases for a patient

diagnose(Patient, Disease) :-
    disease(Disease, Patient).

% ---------- Helper: Add symptoms dynamically ----------
add_symptom(Patient, Symptom) :-
    assertz(symptom(Patient, Symptom)).

clear_symptoms(Patient) :-
    retractall(symptom(Patient, _)).
