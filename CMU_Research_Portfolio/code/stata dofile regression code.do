ssc install estout, replace
ssc install asdoc, replace
cd "D:\Research game addiction\Stata\Output"

* Setup Gender Variable
 capture drop gender_n
 capture confirm string variable gender
 if !_rc {
 	encode gender, gen(gender_n)
 }
 else {
 	gen gender_n = gender
 }
 
 * Model 1
 reg gameaddictiontotal ///
	hoursspend ///
	i.gender_n ///
	i.years ///
	competitiveaction ///
	roleprogression ///
	causalchance ///
	cp1 cp2 cp3 cp4 cp5 cp6 cp7 cp8 cp9, ///
	vce(robust)
est store m1

capture drop resid_model1
predict resid_model1, resid
qnorm resid_model1, name(qq1, replace) ///
	title("Normal Q-Q Plot: Model 1") 
rvfplot, yline(0) name(rvf1, replace)

* Model 2
reg gpa ///
	gameaddictiontotal ///
	cp1 cp2 cp3 cp4 cp5 cp6 cp7 cp8 cp9, ///
	vce(robust)
est store m2

capture drop resid_model2
predict resid_model2, resid
qnorm resid_model2, name(qq2, replace) ///
	title("Normal Q-Q Plot: Model 2")
	
	rvfplot, yline(0) name(rvf2, replace)
	
* Model 3
reg gpa ///
	gameaddictiontotal ///
	hoursspend ///
	i.years ///
	cp1 cp2 cp3 cp4 cp5 cp6 cp7 cp8 cp9, ///
	vce(robust)
est store m3

capture drop resid_model3
predict resid_model3, resid
qnorm resid_model3, name(qq3, replace) ///
	title("Normal Q-Q Plo: Model3")
rvfplot, yline(0) name(rvf3, replace)


* Model 4 (Anova + Post-Hoc)
anova gameaddictiontotal gender_n
est store m4

* Margins mean group
margins gender_n
marginsplot

* Tukey Post-Hoc
pwmean gameaddictiontotal, over(gender_n) mcompare(tukey)
matrix T = r(table)

* Export Regression
esttab m1 m2 m3 m4 using "regression_result.csv", ///
	replace b(3) se(3) ///
	star(* 0.10 ** 0.05 *** 0.01) ///
	stats(N r2, labels("Observation" "R-Squared")) ///
	label nomtitles
	
* Export Tukey
putexcel set "tukey_gender.xlsx", replace
putexcel A1 = ("Comparison"), bold
putexcel B1 = ("Mean Diff."), bold
putexcel C1 = ("SE"), bold
putexcel D1 = ("95% CI (L)"), bold 
putexcel E1 = ("95% CI (U)"), bold
putexcel A2 = matrix(T), names
