// void main()
// {
//   print('Hello, World!');
// }


// Butterfly Pattern using "*"
import 'dart:io';

void main() {
  int n = 5; // Number of rows

  // Upper part of the butterfly
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      stdout.write('* ');
    }
    for (int j = 1; j <= 2 * (n - i); j++) {
      stdout.write('  ');
    }
    for (int j = 1; j <= i; j++) {
      stdout.write('* ');
    }
    print('');
  }

  // Lower part of the butterfly
  for (int i = n; i >= 1; i--) {
    for (int j = 1; j <= i; j++) {
      stdout.write('* ');
    }
    for (int j = 1; j <= 2 * (n - i); j++) {
      stdout.write('  ');
    }
    for (int j = 1; j <= i; j++) {
      stdout.write('* ');
    }
    print('');
  }
}


