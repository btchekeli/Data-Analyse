import 'package:flutter/material.dart';
import 'package:kkiapay_flutter_sdk/kkiapay_flutter_sdk.dart';
import 'package:stripe_payment/stripe_payment.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  StripePayment.setOptions(StripeOptions(
    publishableKey: 'YOUR_STRIPE_PUBLISHABLE_KEY',
  ));
  runApp(const ColisApp());
}

class ColisApp extends StatelessWidget {
  const ColisApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Colis App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  void _payWithKkiapay() {
    KKiaPay.pay(
      context: context,
      amount: 1000,
      phone: '22997000000',
      name: 'John Doe',
      callback: (resp, context) {
        // Handle success or failure
        Navigator.of(context).pop();
      },
    );
  }

  void _payWithStripe() {
    StripePayment.paymentRequestWithCardForm(CardFormPaymentRequest())
        .then((paymentMethod) {
      // Send paymentMethod to server to complete payment
    }).catchError((err) {
      // Handle errors
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Envoyer un colis')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: _payWithKkiapay,
              child: const Text('Payer avec Kkiapay'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: _payWithStripe,
              child: const Text('Payer avec Stripe'),
            ),
          ],
        ),
      ),
    );
  }
}
