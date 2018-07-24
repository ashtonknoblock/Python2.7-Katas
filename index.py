import math
sampleArray = [469, 755, 244, 245, 758, 450, 302, 20, 712, 71, 456, 21, 398, 339, 882, 848, 179, 535, 940, 472]
sampleArray_length = len(sampleArray)

print ' 1. ----------------------------'
for i in range(1,21):
    print i

print ' 2. ----------------------------'
for i in range(1,21):
    if i % 2 == 0:
        print i

print ' 3. ----------------------------'
for i in range(1,21):
    if i % 2 == 1:
        print i

print ' 4. ----------------------------'
for i in range(1,101):
    if i % 5 == 0:
        print i


print ' 5. ----------------------------'
for i in range(1,101):
   if math.sqrt(i) % 1 == 0 :
       print i

print ' 6. ----------------------------'
for i in range(20, 0, -1):
    print i

print ' 7. ----------------------------'
for i in range(20, 0, -1):
    if i % 2 == 0:
        print i

print ' 8. ----------------------------'
for i in range(20, 0, -1):
    if i % 2 == 1:
        print i

print ' 9. ----------------------------'
for i in range(100, 0, -1):
    if i % 5 == 0:
        print i

print ' 10. ----------------------------'
for i in range(100, 0, -1):
    if math.sqrt(i) % 1 == 0 :
       print i

print ' 11. ----------------------------'
for num in sampleArray:
    print num

print ' 12. ----------------------------'
for num in sampleArray:
    if num % 2 == 0:
        print num

print ' 13. ----------------------------'
for num in sampleArray:
    if num % 2 == 1:
        print num

print ' 14. ----------------------------'
for num in sampleArray:
    squared = num * num 
    print squared

print ' 15. ----------------------------'
added = 0
for i in range(0,21):
    added = added + i
print added

print ' 16. ----------------------------'
added = 0
for num in sampleArray:
   added = num + added
print added

print ' 17. ----------------------------'
print min(sampleArray)

print ' 18. ----------------------------'
print max(sampleArray)



    










    