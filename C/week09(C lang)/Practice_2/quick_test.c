#include <stdio.h>
#define MAX_SIZE 100000

float get_max(float * array, int n);
float get_min(float * array, int n);
float get_sum(float * array, int n);
void batchnorm1d(float * array, int n);
int maxpool1d(float * array, int n);


float get_sum(float * array, int n) {
    float sum_val = 0;
    int i;
    for (i= 0; i < n; ++i) {
        sum_val += array[i];
    }
    return sum_val;
}

float get_max(float * array, int n) {
    float max_val = array[0];
    int i;
    for (i = 0; i < n; ++i) {
        if (max_val < array[i]) {
            max_val = array[i];
        }
    }
    return max_val;
}


float get_min(float * array, int n) {
    float min_val = array[0];
    int i;
    for ( i = 0; i < n; ++i) {
        if (min_val > array[i]) {
            min_val = array[i];
        }
    }
    return min_val;
}


void batchnorml1d(float * array, int n)
{
	float max_val = get_max(array, n);
	float min_val = get_min(array, n);
	
	
	int i;
	for (i = 0; i < n; ++i)
	{
		array[i] = (array[i] - min_val ) / (max_val - min_val);
	}
}

int maxpool2d(float * array, int n)
{
	int stride = 1;
	int filter_size = 3;
	int i;
	float result_vector[MAX_SIZE];
	for (i = 0; i < (n - filter_size + 1) / stride; i += stride)
	{
		result_vector[i] = get_max(array + 1, filter_size);
	}
	for(i = 0; i < (n - filter_size + 1) / stride; i += stride)
	{
		array[i] = result_vector[i];
	}
	
	return (n - filter_size + 1)/ stride;
}

int main(void) {
    int N;
    float arr[MAX_SIZE];
    float input_num;
    int i;
    float  max_val, min_val, sum_val;

	scanf("%d", &N);
	
	//input how many numbers you want to save an array
	for(i = 0; i < N; ++i)
	{
		scanf("%f", arr+i);
		//arr[i] = input_num;
	}
	
	//then get an array of numbers
	for(i = 0; i < N ; ++i)
	{
		printf("%f ",arr[i]);
	}
	printf("\n");
    

    printf("max val :%f \n", max_val);
    printf("min val :%f \n", min_val);
    printf("sum val :%f \n", sum_val);
    
    
    batchnorml1d(arr, N);
    printf("After being normalized\n");
    for(i = 0; i < N; ++i)
    {
    	printf("%f ", arr[i]);
	}
	printf("\n");
	
	
	int output_shape = maxpool2d(arr, N);
	printf("After maxpool2d\n");
	for( i = 0; i < output_shape; ++i)
	{
		printf("%f ", arr[i]);
	}
	
	printf("\n");
    //return 0;
}


/*float get_max(float * array, int n)
{
	int i;
	// float max_val = -99999999;
	float max_val = array[0];
	for(i = 0; i < n; ++i)
	{
		
		if(max_val < array[i])
		{
			max_val = array[i];
		}
		
	}
	
	return max_val;
}



float get_min(float * array, int n)
{
	int i;
	// float max_val = -99999999;
	float min_val = array[0];
	for(i = 0; i < n; ++i)
	{
		
		if(min_val > array[i])
		{
			min_val = array[i];
		}
		
	}
	
	return min_val;
}

float get_sum(float * array, int n)
{
	float sum_val = 0;
	int i;
	
	for(i = 0; i < n; ++i)
	{
		sum_val += array[i];
	}
	
	return sum_val;
}

void batchnorm1d(float * array, int n)
{
	float max_val = get_max(array, n);
	float min_val = get_min(array, n);
	
}*/
