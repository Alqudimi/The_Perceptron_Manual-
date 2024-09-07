Perceptron - Loan Approval System

A simple machine learning algorithm using perceptrons to review loan applications. Perceptron_Data.csv`, in this case) This takes the trained model and there parameters for it (we will be using `params/values_full.csv`), then evaluates a user loan request.

---

### How the Code Works

1. **Training the Perceptron:**

The function `Training_My_Perceptron` is the heart of learning by perceptron.

– It takes the input data ( Date_Input), initial weights( Theta) and output labels(Date_Output).

— It modifies the weights (or **theta values**) depending on how wrong it is compared to what was expected, during training.

The aim is to reduce the error so that it can differentiate between authorized & notok loans correctly(inputs).

2. **Weight Adjustment:**

- In the `Weight_Adjustment` function, we update the weights based on whether our perceptron correctly identifies data.

This continues in iteration, until the perceptron is able to predict whether a loan will be granted or denied correctly.

3. **Using the Perceptron:**

UseOfThe_MyPerceptron (*): enters new demands after training.

Optoisolaters in the user, such as salary, working hours and others.

Use the system trained perceptron to decide if the loan is approved or denied.

---

### How to Use the Program

1. **Data Preparation:**

1) Create one Csv file name Perceptron_Data. csv` with your training data.

- A file, which should have columns for things like salary and working hours among other relevant features.

The last column of the file should be the ground truth value (1 approved loans, 0 denied loan).

2. **Training the Perceptron:**

Now, the program is going to read data from `Perceptron_Data`. csv`.

The system trains itself with the provided data to adjusting weights in order move closer and minimize errors (which was calculated previously).
   
3. **Request Evaluation:**

– System will ask how many Loan requests you want to process after training.

– When you complete the form, it will ask for details of each request (salary/hours worked etc..).

That process will take a few minutes, after which the system will tell you if your loan is approved or not.

4. **Conclusion:**

- In simple words, this model is a perceptron which mainly serves to teach machine learning because it makes use of the binary class data that are in reality provided for loan approval.

Proper care should be taken regarding your training data, even a slight mistake will lead them Model to destruction.

---

