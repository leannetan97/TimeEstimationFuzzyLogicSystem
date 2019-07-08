# Time Estimation Fuzzy Logic System <br>(Soft Computing Assignment WIX3001)
This is a Clinic Time Estimation System using Fuzzy Logic Concept.

<p><b>There are 2 folders for the Clinic Time Estimation System:</b><br>
1. Fuzzy Logic System (using SKFuzzy Library)<br>
2. Fuzzy Logic System (without using SKFuzzy Library)<br>
</p>

<h3>To install the dependencies:</h3>
<p>
1. Download the requirements.txt <br>
2. Intsall using <b>pip install  --no-cache-dir -r requirements.txt</b> or <b>pip install -r requirements.txt</b>.
</p><br>


<h3>General Fuzzy Logic Algorithm</h3>
<p>
  1. Define the linguistic variables and terms (initialization)<br>
  2. Construct the membership functions (initialization)<br>
  3. Construct the rule base (initialization)<br>
  4. Convert crisp input data to fuzzy valuesusing the membership functions (fuzzification)<br>
  5. Evaluate the rules in the rule base (inference)<br>
  6. Combine the results of each rule (inference)<br>
  7. Convert the output data to non-fuzzy values (defuzzification)
  </p><br>
<h3> Crisp Input & Output </h3>
<p><b>The crisp input are:</b><br>
&nbsp1. Doctor's availability [0-10]<br>
&nbsp2. Length of the queue [0-10]<br>
<br>
<b>The crisp output are:</b><br>
&nbsp1. Time Estimation [0-30min]</p>
