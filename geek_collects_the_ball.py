for _ in range(int(input())):
      n,m = map(int,input().split())
      a = [int(x) for x in input().split()]
      b = [int(x) for x in input().split()]
      ans, sum1, sum2, j, k = 0, 0, 0, 0, 0
      while j < n and k < m:
          if a[j] < b[k]:
              sum1 += a[j]
              j+=1
          elif b[k] < a[j]:
              sum2 += b[k]
              k+=1
          else:
              sum1 += a[j]
              sum2 += b[k]
              j += 1
              k += 1
              ans += max(sum1,sum2)
              sum1, sum2 = 0, 0
      while j < n:
            sum1+=a[j]
            j+=1

      while k < m:
            sum2 += b[k]
            k += 1
      ans += max(sum1,sum2)
      print(ans)
                  
              
