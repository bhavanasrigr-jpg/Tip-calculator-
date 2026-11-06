
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Tip Calculator',
      theme: ThemeData(
        colorSchemeSeed: Colors.deepPurple,
        useMaterial3: true,
      ),
      home: const TipCalculator(),
    );
  }
}

class TipCalculator extends StatefulWidget {
  const TipCalculator({super.key});

  @override
  State<TipCalculator> createState() => _TipCalculatorState();
}

class _TipCalculatorState extends State<TipCalculator> {
  final TextEditingController billController =
      TextEditingController();

  double tipPercentage = 10;
  int people = 1;

  double get billAmount =>
      double.tryParse(billController.text) ?? 0;

  double get tipAmount =>
      billAmount * tipPercentage / 100;

  double get totalAmount =>
      billAmount + tipAmount;

  double get perPerson =>
      people > 0 ? totalAmount / people : 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey.shade100,
      appBar: AppBar(
        title: const Text('Tip Calculator'),
        centerTitle: true,
        backgroundColor: Colors.deepPurple,
        foregroundColor: Colors.white,
      ),

      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Icon(
              Icons.calculate,
              size: 75,
              color: Colors.deepPurple,
            ),

            const SizedBox(height: 20),

            const Text(
              'Calculate Your Bill',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 23,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 25),

            // BILL AMOUNT

            TextField(
              controller: billController,
              keyboardType: const TextInputType.numberWithOptions(
                decimal: true,
              ),
              onChanged: (value) {
                setState(() {});
              },
              decoration: const InputDecoration(
                labelText: 'Enter Bill Amount',
                prefixIcon: Icon(Icons.currency_rupee),
                border: OutlineInputBorder(),
              ),
            ),

            const SizedBox(height: 25),

            // TIP SLIDER

            Text(
              'Tip Percentage: ${tipPercentage.round()}%',
              style: const TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),

            Slider(
              value: tipPercentage,
              min: 0,
              max: 30,
              divisions: 30,
              label: '${tipPercentage.round()}%',
              activeColor: Colors.deepPurple,
              onChanged: (value) {
                setState(() {
                  tipPercentage = value;
                });
              },
            ),

            const SizedBox(height: 20),

            // SPLIT BETWEEN PEOPLE

            const Text(
              'Split Between People',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 12),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                IconButton(
                  onPressed: () {
                    if (people > 1) {
                      setState(() {
                        people--;
                      });
                    }
                  },
                  icon: const Icon(Icons.remove_circle),
                  color: Colors.deepPurple,
                  iconSize: 35,
                ),

                Text(
                  '$people',
                  style: const TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),

                IconButton(
                  onPressed: () {
                    setState(() {
                      people++;
                    });
                  },
                  icon: const Icon(Icons.add_circle),
                  color: Colors.deepPurple,
                  iconSize: 35,
                ),
              ],
            ),

            const SizedBox(height: 25),

            // RESULTS

            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.deepPurple.shade50,
                borderRadius: BorderRadius.circular(18),
              ),
              child: Column(
                children: [
                  resultRow(
                    'Tip Amount',
                    tipAmount,
                  ),

                  const Divider(),

                  resultRow(
                    'Total Bill',
                    totalAmount,
                  ),

                  const Divider(),

                  resultRow(
                    'Each Person Pays',
                    perPerson,
                    highlight: true,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget resultRow(
    String title,
    double amount, {
    bool highlight = false,
  }) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 12),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(
            child: Text(
              title,
              style: TextStyle(
                fontSize: highlight ? 17 : 15,
                fontWeight: highlight
                    ? FontWeight.bold
                    : FontWeight.normal,
              ),
            ),
          ),
          Text(
            '₹${amount.toStringAsFixed(2)}',
            style: TextStyle(
              fontSize: highlight ? 21 : 17,
              fontWeight: FontWeight.bold,
              color: Colors.deepPurple,
            ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    billController.dispose();
    super.dispose();
  }
}
