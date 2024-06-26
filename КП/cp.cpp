#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <queue>
#include <stack>
#include <numeric>
#include <set>

using namespace std;

double PI = acos(-1);

double func(double x) {
	return sin(x);
}

vector<vector<double>> transp(vector<vector<double>> A) {
	int n = A.size();
	vector<vector<double>> B(n, vector<double> (n));
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			B[i][j] = A[j][i];
		}
	}
	return B;
}

vector<vector<double>> matr_coef(int n) {
	vector<vector<double>> B(n, vector<double>(n));
	for (int i = 0;i < n / 2;i++) {
		B[i][i * 2] = 1 / sqrt(2);
		B[i][i * 2 + 1] = 1 / sqrt(2);
		B[i + n / 2][i * 2] = 1 / sqrt(2);
		B[i + n / 2][i * 2 + 1] = -1 / sqrt(2);
	}
	return B;
}

double g;
int N;
double h;

void get_c_and_d(int n, vector<double> &fin_d, vector<double> x) {
	if (n == 1) {
		g = x[0];
		return;
	}
	vector<vector<double>> A = matr_coef(n);
	vector<double> c;
	for (int i = 0;i < n / 2;i++) {
		double tmp = 0;
		for (int j = 0;j < n;j++) {
			tmp = tmp + A[i][j] * x[j];
		}
		c.push_back(tmp);
	}
	vector<double> d1;
	for (int i = n / 2;i < n;i++) {
		double tmp = 0;
		for (int j = 0;j < n;j++) {
			tmp = tmp + A[i][j] * x[j];
		}
		d1.push_back(tmp);
	}

	if (n > 4) {
		for (int i = 0;i < N;i = i + N / n * 2) {
			cout << i * h << ' ';
		}
		cout << '\n';
		for (int i = 0;i < c.size();i++) {
			cout << c[i] << ' ';
		}
		cout << '\n';
		for (int i = 0;i < N;i = i + N / n * 2) {
			cout << i * h << ' ';
		}
		cout << '\n';
		for (int i = 0;i < d1.size();i++) {
			cout << d1[i] << ' ';
		}
		cout << '\n';
	}

	for (int i = 0;i < fin_d.size();i++) {
		d1.push_back(fin_d[i]);
	}
	fin_d = d1;
	get_c_and_d(n / 2, fin_d, c);
}

vector<double> get_vals(int n, double c, vector<double> d) {
	vector<double> cur;
	cur.push_back(c);
	cur.push_back(d[0]);
	int k = 1;
	while (true) {
		int n1 = cur.size();
		vector<vector<double>> A = matr_coef(n1);
		vector<vector<double>> B = transp(A);						// обратная
		vector<double> cur1;
		for (int i = 0;i < n1;i++) {
			double tmp = 0;
			for (int j = 0;j < n1;j++) {
				tmp = tmp + B[i][j] * cur[j];
			}
			cur1.push_back(tmp);
		}
		n1 = cur1.size();
		if (n1 == n) {
			cur = cur1;
			break;
		}
		for (int i = k; i < k + n1; i++) {
			cur1.push_back(d[i]);
		}
		cur = cur1;
		k = k + n1;
	}
	return cur;
}

void veivlet(int n, double l) {
	N = n;
	h = l / n;
	vector<double> x;
	for (int i = 0;i < n;i++) {
		x.push_back(func(i * h));
	}
	vector<double> d;
	get_c_and_d(n, d, x);
	double c = g;
	vector<double> x1 = get_vals(n, c, d);

	for (int i = 0;i < n;i++) {
		cout << i * h << ' ';
	}
	cout << '\n';
	for (int i = 0;i < n;i++) {
		cout << x[i] << ' ';
	}
	cout << '\n';
	for (int i = 0;i < n;i++) {
		cout << i * h << ' ';
	}
	cout << '\n';
	for (int i = 0;i < n;i++) {
		cout << x1[i] << ' ';
	}
}


int main() {
	veivlet(32, 2 * PI);
}
