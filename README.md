## M lang
### The simple language created for easy matrix computations. The project is based on yacc and lex.

#### Syntax presentation:

##### Bubble sort

```
array = [5,4,1,2,3,5,7,11];
n = 8;
for i = 0:n {
    upper_bound = n - i - 1;
    for j = 0:upper_bound {
        next = j + 1;
        if (array[j] > array[next]){
            tmp = array[next];
            array[next] = array[j];
            array[j] = tmp;
        }
    }
}

print array;
```

#### Matrix operations

```
a = [1,2,3;
    4,5,6;
    7,8,9];
b = [9,8,7;
    6,5,4;
    3,2,1];
    
x = a * b;
print x;

y = a + b;
print y;

# Support for element-wise operations
y = a .* b;
print y;
```
