#!/bin/python
# 
# Математические основы
#    Системы счисления
#    Метод индукции
#    Логарифмы 
#    Алгоритмическая сложность 
#    Рекурентный анализ (возможно этот пункт стоит расскрыть после введения понятия рекурсия)
#    Базовые понятия теории вероятности и математической статистики
#      Зачем нужна теория вероятности в изучении алгоритмов?
#      Классическое определение вероятности
#      Мода, медиана и моменты
#         Cреднее арифметическое, дисперсия, асимметрия и эксцесс
#      Основные законы распределения
# Основы Python
# Установка Python3 
#    Установка в Windows
#    Установка в Linux 
# Типы данных
#    Примитивные типы данных 
#       Целочисленные данные
#       Действительные данные
#       Строковые данные
#       Булевые (логические) данные
#    Сложные типы данных
#       Кортежи
#       Множества
#       Ассоциативные массивы (словари или хеш таблицы)
#       Мыссивы
#       Классы
#       Инумерации
# Переменные
# b = True
# i = 5
# s = "Это моя строковая переменная"
# d = 0.9
# s = set([4, 5, 2]);
# m = dict({"ключ1": "значение1"})
# o = MyClass();
# с = (0, 2)

# Операторы
# Бинарные операторы
#   Сложение 
#   Вычитание
#   Умножение
#   Деление
#   Остаток от деления
#   Логические операторы (and, or, not, xor (nor a or not b), == (equivalence), implication)
# Унарные операторы
# Приоритеты операторов
# Выражения
# Примеры
# r = 10 + 1
# r = a + 1
# r = a * b
# r = a / b
# Циклы
# for
# while 
# Прерывание циклов (break, return)
# Продолжение цикла (continue)
# Возврат значения из цикла (yield)
# Перебор массивов с индексом (enumerate)
# Операторы ветвления
# if elif else
# 
# Функции
#   Объявление функций
#   Возврат из функции (return)
#   Передача параметров по значению и по ссылке
#   
# Классы
# Перечисления
#
# Основные структуры данных
#   Множества
#   Массивы
#   Хеш таблицы (ассоциативные таблицы)
#   Очереди 
#   Стеки
#   Кучи
#   Деревья
#     Бинарные деревья
#     Сбалансированные бинарные деревья
#     Обход дерева вглубь и вширь
#   Графы
#     Направленные графы
#     Ненаправленные графы
#     Представление графов в Python
#     Обход графов
#     Поиск наикротчайшего пути между двумя вершинами
#   
# Базовые алгоритмы
#   Разделяй и влавствуй
#   Сортировка
#     Сортировка вставками
#     Сортировка слиянием
#     Быстрая сортировка
#     Сортировка кучей
#   Жадные алгоритмы
#     Алгоритм Хафмана
#   Динамическое программирование



# Сортировка слиянием

from math import floor, ceil

a=[2, 4, 5, 1, 9, 0, 10, -1, 7, 7, 0, -2, -5, 12]

def merge(a, b):
	c = []
	h = 0
	l = 0
	while h < len(a) and l < len(b):
		if a[h] < b[l]:
			c.append(a[h])
			h += 1
		else:
			c.append(b[l])
			l += 1
	if h < len(a):
		for j in range(h, len(a)):
			c.append(a[j])
	if l < len(b):
		for j in range(l, len(b)):
			c.append(b[j])
	return c

def merge_sort(a):
	if len(a) <= 1:
		return a;
	midpoint = floor(len(a) / 2);
	w = merge_sort(a[0:midpoint]);
	v = merge_sort(a[midpoint:len(a)]);
	return merge(w, v);

# Быстрая сортировка
def quicksort(a):
	if len(a) == 1:
		return a;
	if len(a) == 0:
		return [];
	midpoint = floor(len(a) / 2);
	smaller = [];
	larger  = [];
	for i in range(0, len(a)):
		if i == midpoint:
			continue;
		if a[midpoint] > a[i]:
			smaller.append(a[i]);
		if a[midpoint] <= a[i]:
			larger.append(a[i]);
	left = quicksort(smaller);
	right = quicksort(larger);
	return left + [a[midpoint]] + right;

# Analysis of the quicksort
# 
# T(N)   = 2T(N/2) + N
# T(N/2) = 2T(N/4) + N/2
# T(N/4) = 2T(N/8) + N/4
# ...
# T(N) = 2(2T(N/4) + N/2) + N
#      = 4T(N/4) + 2N
#      = 8T(N/8) + 3N
#      ...
#      = 2^iT(N/2^i) + iN
#      N/2^i = 1 => N = 2^i => i = logN
#      = N + NLogN
#      = O(NLogN)

# Сортировка вставками
# Сложность алгоритма O(n^2)
def insertion_sort(a):
	for i in range(0, len(a)):
		for j in range(i, len(a)):
			if a[i] > a[j]:
				s = a[i];
				a[i] = a[j]
				a[j] = s
	return a

# Binary search over sorted array
# Сложность алгоритма O(log(n))
def binary_search(a, v):
	a = quicksort(a);
	target = v;
	start = 0;
	end = len(a) - 1;
	if len(a) == 0:
		return None
	while True:
		if end - start == 1 or end == start:
			if a[start] == v:
				return (start, v)
			elif a[end] == v:
				return (end, v)
			else:
				return None
		mid_point = floor((end + start) / 2)
		if target < a[mid_point]:
			end = mid_point;
		elif target > a[mid_point]:
			start = mid_point;
		elif target == a[mid_point]:
			return (mid_point, v);

# Сложность O(n log(n)) для поиска
# 
# T(n) = 2T(n/2) + n
# T(n/2) = 2T(n/4) + n / 2
# T(n/4) = 2T(n/8) + n / 4
# ...
# T(n) = 2(2T(n/4) + n / 2) + n 
#      = 4T(n/4) + 2n
#      = 4(2T(n/8) + n / 4) + 2n
#      = 8T(n/8) + 3n
#      ...
#      = 2^i T(n/2^i) + in
#      Let
#      n = 2^i
#      i = log(n)
#      = 2^log(n) + n log(n)
#      But,
#      log(n) = i => 2^i = n
#      = n + n log(n) = O(n log(n))
# Сложность для поиска максимума O(1)
# Сложность для восстановления дерева O(log(n))

class heap():
	def __init__(self):
		self.h = [0];
		self.length = 0;

	def size(self):
		return self.length;

	def _down(self):
		c = 1;
		while c * 2 <= self.length:
			if c * 2 + 1 <= self.length:
				if self.h[c * 2] < self.h[c * 2 + 1] and self.h[c] < self.h[c * 2 + 1]:
					v = self.h[c];
					self.h[c] = self.h[c * 2 + 1];
					self.h[c * 2 + 1] = v;
					c = c * 2 + 1;
				elif self.h[c] < self.h[c * 2]:
					v = self.h[c];
					self.h[c] = self.h[c * 2];
					self.h[c * 2] = v;
					c = c * 2;
				else:
					break;
			else:
				if self.h[c] < self.h[c * 2]:
					v = self.h[c];
					self.h[c] = self.h[c * 2];
					self.h[c * 2] = v;
					c = c * 2;
				else:
					break;

	def _up(self):
		c = self.length;
		while c > 1 and self.h[c] > self.h[floor(c / 2)]:
			v = self.h[c];
			self.h[c] = self.h[floor(c / 2)];
			self.h[floor(c / 2)] = v;
			c = floor(c / 2);

	def pop(self):
		if self.length == 0:
			return None;
		self.length -= 1;
		v = self.h[1];
		if self.length == 0:
			self.h = [0];
			return v;
		self.h[1] = self.h[len(self.h) - 1];
		self.h = self.h[0:len(self.h) - 1];
		self._down();
		return v;

	def push(self, v):
		self.length += 1;
		self.h.append(v);
		self._up();

	def print(self):
		#print(self.length);
		print(self.h[1:self.length + 1]);
		#print(self.h)
class hitem():
	def __init__(self, value, cost):
		self.value = value;
		self.cost = cost;


class min_heap():
	def __init__(self):
		self.h = [0];
		self.length = 0;

	def size(self):
		return self.length;

	def _down(self):
		c = 1;
		while c * 2 <= self.length:
			if c * 2 + 1 <= self.length:
				if self.h[c * 2].value < self.h[c * 2 + 1].value and self.h[c].value > self.h[c * 2 + 1].value:
					v = self.h[c];
					self.h[c] = self.h[c * 2 + 1];
					self.h[c * 2 + 1] = v;
					c = c * 2 + 1;
				elif self.h[c].value > self.h[c * 2].value:
					v = self.h[c];
					self.h[c] = self.h[c * 2];
					self.h[c * 2] = v;
					c = c * 2;
				else:
					break;
			else:
				if self.h[c].value > self.h[c * 2].value:
					v = self.h[c];
					self.h[c] = self.h[c * 2];
					self.h[c * 2] = v;
					c = c * 2;
				else:
					break;

	def _up(self):
		c = self.length;
		while c > 1 and self.h[c].value < self.h[floor(c / 2)].value:
			v = self.h[c];
			self.h[c] = self.h[floor(c / 2)];
			self.h[floor(c / 2)] = v;
			c = floor(c / 2);

	def pop(self):
		if self.length == 0:
			return None;
		self.length -= 1;
		v = self.h[1];
		if self.length == 0:
			self.h = [0];
			return v;
		self.h[1] = self.h[len(self.h) - 1];
		self.h = self.h[0:len(self.h) - 1];
		self._down();
		return v;

	def push(self, v):
		self.length += 1;
		self.h.append(v);
		self._up();

	def print(self):
		#print(self.length);
		print(self.h[1:self.length + 1]);
		#print(self.h)

def heap_sort(a):
	h = heap();
	for i in a:
		h.push(i);
	b = [];
	for i in range(0, h.size()):
		b.append(h.pop());
	b.reverse()
	return b;

class litem():
	def __init__(self, value):
		self.next = None;
		self.prev = None;
		self.value = value;

class linked_list():

	def __init__(self):
		self.head = None;
		self.tail = None;
		self.length = 0;

	def size(self):
		return self.length;

	def add(self, item):
		if not isinstance(item, litem):
			raise Exception("Invalid type for item");
		self.length += 1;
		if not self.head and not self.tail:
			self.head = item;
			self.tail = item;
			item.prev = None;
			item.next = None;
			return;
		item.prev = self.tail;
		item.next = None;
		self.tail.next = item;
		self.tail = item;

	def get(self, index):
		if index < 0 or index > self.length:
			raise Exception("Index out of range");
		item = self.head;
		prev = None;
		current_index = 0;
		while item != None:
			if current_index == index:
				return item;
			current_index += 1;
			item = item.next;

	def remove(self, index):
		if index < 0 or index > self.length:
			raise Exception("Index out of range");
		item = self.head;
		prev = None;
		current_index = 0;
		while item != None:
			if current_index == index:
				self.length -= 1;
				if item == self.head:
					if item == self.tail:
						self.head = self.tail = None;
					else:
						self.head = item.next;
						self.head.prev = None;
					return item;
				elif item == self.tail:
					self.tail = self.tail.prev;
					self.tail.next = None;
					return item;
				else:
					prev = item.prev;
					next = item.next;
					prev.next = next;
					next.prev = prev;
					return item;
			current_index += 1;
			item = item.next;

	def iterate(self):
		i = self.head;
		while i != None:
			yield i.value;
			i = i.next;

class stack():
	def __init__(self):
		self.ll = linked_list();
	def push(self, value):
		self.ll.add(litem(value));
	def pop(self):
		length = self.ll.size();
		if length == 0:
			raise Exception("Stack is empty");
		return self.ll.remove(length - 1).value;
	def top(self):
		length = self.ll.size();
		if length == 0:
			raise Exception("Stack is empty");
		return self.ll.get(length - 1).value;

class queue():
	def __init__(self):
		self.ll = linked_list();
	def enqueue(self, value):
		self.ll.add(litem(value));
	def dequeue(self):
		return self.ll.remove(0).value;

class priority_queue():
	def __init__(self):
		self.h = heap();
	def enqueue(self, value):
		self.h.push(value);
	def dequeue(self):
		return self.h.pop();

class item():

	def __init__(self, k, v):
		self.k = k;
		self.v = v;

	def key(self):
		return self.k;

	def value(self):
		return self.v;

# The assumption is such that the keys are distributed uniformly
class hash_table():

	def __init__(self, size = 10):
		self.table_size = size;
		self.table = [0] * self.table_size;

	def add(self, k, v):
		if self.get(k) != None:
			return;
		_k = k % self.table_size;
		if not isinstance(self.table[_k], list):
			self.table[_k] = list();
		self.table[_k].append(item(k, v));

	def get(self, k):
		_k = k % self.table_size;
		if not isinstance(self.table[_k], list):
			return None;
		for i in self.table[_k]:
			if i.key() == k:
				return i.value();
		return None

class hash_table_lp():

	def __init__(self, size = 100):
		self.table_size = size;
		self.fill_level = 0;
		self.table = [0] * self.table_size;

	def hash(self, k):
		# If the key is not a number, then hashing should be done in such a manner so that 
		# the keys are distributed uniformly
		return k % self.table_size;

	def add(self, k, v):
		if self.get(k) != None:
			return;
		_k = self.hash(k);
		# After 1 insert: Collision probability 1/size 
		# After 2 inserts: Collision probability 2/size
		# After 3 inserts: Collision probability 3/size
		# ...
		# After n inserts: Collision probability n/size
		# The algorithm becomes inefficient after size/2 inserts?
		while True:
			#self.table[_k].append(item(k, v));
			if self.table[_k] == 0:
				self.table[_k] = item(k, v);
				self.fill_level += 1;
				break;
			_k = self.hash(_k + 1);

	def get(self, k):
		_k = self.hash(k);
		c = 0;
		while True:
			i = self.table[_k];
			if i == 0:
				return None	
			if i.key() == k:
				return i.value();
			c += 1;
			if c == self.table_size:
				break;
			_k = self.hash(_k + 1);
		return None

	def remove(self, k):
		_k = self.hash(k);
		c = 0;
		while True:
			i = self.table[_k];
			if i != 0 and i.key() == k:
				self.table[_k] = 0;
				return True;
			c += 1;
			if c == self.table_size:
				break;
			_k = self.hash(_k + 1);
		return False

# Main property of a binary search tree
# is that the left subtree has values are
# smaller than value of a root element, 
# and the values in the right subtree are 
# larger than value in the root node. 
class binary_search_tree():
	def __init__(self):
		self.tree = [];
	def add_node(self, v):
		self.tree.append(v);
	def traverse(self):
		pass

# Longest common substring: dynamic programming approach
# Сложность алгоритма O(nm)
# https://www.techiedelight.com/longest-common-substring-problem/
#     +---+---+---+---+---+
#     |   | A | B | C | A |
# +---+---+---+---+---+---+
# |   | 0 | 0 | 0 | 0 | 0 |
# +---+---+---+---+---+---+
# | A | 0 | 1 | 0 | 0 | 1 |
# +---+---+---+---+---+---+
# | B | 0 | 0 | 2 | 0 | 0 |
# +---+---+---+---+---+---+
# | A | 0 | 1 | 0 | 0 | 1 |
# +---+---+---+---+---+---+
# This is rather understandable
def LCS(a, b):
	table = [0] * (len(a) + 1);
	for i in range(0, len(a) + 1):
		table[i] = [0] * (len(b) + 1);
	max_length = 0;
	end = 0;
	for i in range(1, len(a) + 1):
		for j in range(1, len(b) + 1):
			if a[i - 1] == b[j - 1]:
				table[i][j] = table[i - 1][j - 1] + 1;
				if table[i][j] > max_length:
					max_length = table[i][j];
					end = i;
	return a[end - max_length:end];

# Shortest path search 
def FWA(adj, s, d):
	# adj - adjacency matrix
	# s   - source
	# d   - destination
	# Mind blowing algorithm
	pass

from math import inf

def a_star_search(graph, start, end):
	h = min_heap();
	cost_so_far = [inf] * len(graph);
	came_from = dict();
	h.push(hitem(start, 0));
	cost_so_far[start] = 0;

	while h.size() > 0:
		current = h.pop();
		if current.value == end:
			break;
		for i in range(0, len(graph[current.value])):
			if graph[current.value][i] == 0:
				continue;
			new_cost = cost_so_far[current.value] + graph[current.value][i];
			if new_cost < cost_so_far[i]: 
				cost_so_far[i] = new_cost;
				h.push(hitem(i, new_cost));
				came_from[i] = current.value;
	return came_from;

class TreeNode():
	def __init__(self, key):
		self.key = key;
		self.height = 1;
		self.left = None;
		self.right = None;
	def __str__(self):
		return str(self.key);

class AVLTree():
	def search(self, root, key):
		if not root:
			return False;
		if key == root.key:
			return True;
		if key > root.key:
			return self.search(root.right, key);
		else:
			return self.search(root.left, key);

	def insert(self, key, root):
		if not root:
			return TreeNode(key);
		if key > root.key:
			root.right = self.insert(key, root.right);
		elif key < root.key:
			root.left = self.insert(key, root.left);
		else:
			return root;

		root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1;
		balance = self.get_height(root.left) - self.get_height(root.right);

		if balance > 1 and key < root.left.key:
			root = self.rotate_right(root);
		if balance < -1 and key > root.right.key:
			root = self.rotate_left(root);
		if balance > 1 and key > root.left.key:
			root.left = self.rotate_left(root.left);
			root = self.rotate_right(root);
		if balance < -1 and key < root.right.key:
			root.right = self.rotate_right(root.right);
			root = self.rotate_left(root);
		return root;

	def rotate_left(self, root):
		z = root;
		y = root.right;		
		z.right = y.left;
		y.left = z;
		z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1;
		y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1;
		return y;

	def rotate_right(self, root):
		z = root;
		y = root.left;		
		z.left = y.right;
		y.right = z;
		z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1;
		y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1;
		return y;

	def get_height(self, root):
		if not root:
			return 0;
		return root.height;

	def balance(self, left, right):
		return self.get_height(left) - self.get_height(right);

def dijkstra(adj, weights, a):
	d = [i for i in range(0, len(adj))];
	for i in d:
		d[i] = 1e10;
	d[a] = 0;
	U = [a];
	V = [];
	p = [None] * len(d);
	p[a] = [0];
	while len(U) != 0:
		v = U[0];
		U = U[1:];
		V.append(v);
		for j in range (0, len(d)):
			if adj[v][j] == 0:
				continue;
			if j in V:
				continue;
			U.append(j);
			if d[j] > d[v] + weights[v][j]:
				d[j] = d[v] + weights[v][j]
				p[j] = p[v] + [j];
	return (d, p)

print("--------------Min heap --------------");
h = min_heap();
h.push(hitem(10, 0));
h.push(hitem(5, 0));
h.push(hitem(100, 0));
h.push(hitem(-5, 0));
h.push(hitem(20, 0));

print(h.pop().value);
print(h.pop().value);
print(h.pop().value);
print(h.pop().value);
print(h.pop().value);

print("------------ A* search algorithm-------------");
graph=[[0, 1, 3, 0], [1, 0, 1, 3], [3, 1, 0, 1], [0, 3, 1, 0]];
print(a_star_search(graph, 0, 3));


#[0, 1, 4, 5, 8]

print("------------Merge sort--------------");
print(merge_sort(a));
# 
# Сложность O(n^2)
print('------------Insertion sort-------------');
print(insertion_sort(a));

print('------------Heap sort-------------------');
print(heap_sort(a));

print('------------Quicksort-------------------');
print(quicksort(a));

print("------------Heap--------------");
h = heap();
h.push(9);
#h.print();
h.push(10);
#h.print();
h.push(8);
#h.print();
h.push(1);
h.push(11);
#h.print();
print(h.pop());
print(h.pop());
print(h.pop());
print(h.pop());
print(h.pop());
#print(h.pop())
h.push(-1);
h.push(100);
#h.print();
h.push(1);
h.push(11);
#h.print();
h.push(0);
#h.print();
print(h.pop());
print(h.pop());
print(h.pop());
print(h.pop());
print(h.pop());

print("------------ Hash table --------------");
ht = hash_table();
ht.add(19, 19);
print("key = 19,  value = ", ht.get(19));
ht.add(119, 119);
ht.add(1, 1);
ht.add(12, 12);
ht.add(73, 73);
print("key = 119, value = ", ht.get(119));

print("------------ Hash table with linear probing ---------------");
ht = hash_table_lp(100);
ht.add(19, 19);
print("key = 19,  value = ", ht.get(19));
ht.add(119, 119);
ht.add(1, 1);
ht.add(12, 12);
ht.add(73, 73);
print("key = 119, value = ", ht.get(119));

print("------------ Linked list --------------");

ll = linked_list();
ll.add(litem(10));
ll.add(litem(9));
ll.add(litem(1));
ll.add(litem(11));

for v in ll.iterate():
	print(v)

ll.remove(0);

for v in ll.iterate():
	print(v)

print("---------------- Queue ----------------");
q = queue();
q.enqueue(10);  
q.enqueue(100); 
q.enqueue(1000);
print(q.dequeue());
print(q.dequeue());
print(q.dequeue()); 

print("---------------- Priority queue ----------------- ");
pq = priority_queue();
pq.enqueue(10);
pq.enqueue(12);
pq.enqueue(44);
pq.enqueue(0);
pq.enqueue(100);
print(pq.dequeue());
print(pq.dequeue());
print(pq.dequeue());
print(pq.dequeue());
print(pq.dequeue());

print("--------------- Stack ---------------------------- ");
s = stack();
s.push(10);
s.push(100);
s.push(-1);
s.push(2);
print(s.top());
print(s.pop());
print(s.top());
print(s.pop());
print(s.top());
print(s.pop());
print(s.top());
print(s.pop());
#print(s.top());
#print(s.pop());
#print(s.top());
print("-------------------- Longest common substring (dynamic programming) ---------------------");
print(LCS("abax", "bax"));
print("--------------- Divide and conquer (binary search) ------------------------------");
print(binary_search([-1, 5, 10, 2, 0, 4, 5, 1, 2, 5, 1, 4, 12, 20, 3], 15));

print("-------------------- AVL tree -----------------------");
root = None;
tree = AVLTree();
root = tree.insert(1, root);
root = tree.insert(2, root);
root = tree.insert(11, root);
root = tree.insert(3, root);
root = tree.insert(6, root);
root = tree.insert(22, root);
root = tree.insert(14, root);
root = tree.insert(0, root);
print("Searching key 22");
print(tree.search(root, 22));

root = None;
tree = AVLTree();
root = tree.insert(4, root);
root = tree.insert(2, root);
root = tree.insert(5, root);
root = tree.insert(1, root);
root = tree.insert(3, root);
root = tree.insert(0, root);
print(root.height);

print("Searching key 0");
print(tree.search(root, 0));

adj = [[0, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 0, 0],
		[1, 1, 0, 1, 0, 1],
		[0, 1, 1, 0, 1, 0],
		[0, 0, 0, 1, 0, 1],
		[1, 0, 1, 0, 1, 0]];

weights = [[0, 7, 9, 0, 0, 14],
		[7, 0, 10, 15, 0, 0],
		[9, 10, 0, 11, 0, 2],
		[0, 15, 11, 0, 6, 0],
		[0, 0, 0, 6, 0, 6],
		[14, 0, 2, 0, 9, 0]]; 

print("----------------Dijkstra search ----------------");
print(dijkstra(adj, weights, 0));


ll = linked_list();
ll.add(litem(10));
ll.add(litem(11));
ll.add(litem(12));
ll.add(litem(0));
for i in ll.iterate():
	print(i);
