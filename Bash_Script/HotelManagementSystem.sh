#!/bin/sh
menu_choice=""
record_file="bookRecords.ldb"
temp_file=/tmp/ldb.$$
touch $temp_file; chmod 644 $temp_file
trap 'rm -f $temp_file' EXIT


get_return(){
printf '\tPress return\n'
read x
return 0
}

get_confirm(){
printf '\tAre you sure?\n'
while true
do
  read x
  case "$x" in
      y|yes|Y|Yes|YES)
      return 0;;
      n|no|N|No|NO)
          printf '\ncancelled\n'
          return 1;;
      *) printf 'Please enter yes or no\n';;
  esac
done
}

set_menu_choice(){
clear
printf 'Options:-'
printf '\n'
printf '\ta) Add new Customer records\n'
printf '\tb) Find Customer Data\n'
printf '\tc) Edit Customer Data\n'
printf '\td) Remove Customer Data\n'
printf '\te) View Customer Record\n'
printf '\tf) Quit\n'
printf 'Please enter the choice then press return\n'
read menu_choice
return
}

insert_record(){
echo $* >>$record_file
return
}


#!!!!!!!!!...........................!!!!!!!!!!!!!!!!
#This function ask user for details information about Customer for keeping records

add_books(){

#prompt for information

printf 'Enter Customer Name:-'
read tmp
liCatNum=${tmp%%,*}

printf 'Enter Check-in Details:-'
read tmp
liTitleNum=${tmp%%,*}

printf 'Enter Room Number:-'
read tmp
liAutherNum=${tmp%%,*}

#Check that they want to enter the information
printf 'About to add new entry\n'
printf "$liCatNum\t$liTitleNum\t$liAutherNum\n"

#If confirmed then append it to the record file
if get_confirm; then
   insert_record $liCatNum     \t     ,          $liTitleNum     \t     ,     \t     $liAutherNum
fi

return
}

find_books(){
  echo "Enter Customer Name to find:"
  read book2find
  grep $book2find $record_file > $temp_file

  # set $(wc -l $temp_file)
  # linesfound=$1
  linesfound=`cat $temp_file|wc -l`

  case `echo $linesfound` in
  0)    echo "Sorry, nothing found"
        get_return
        return 0
        ;;
  *)    echo "Found the following"
        cat $temp_file
        get_return
        return 0
  esac
return
}

remove_books() {
# $temp_file

  #set $(wc -l $temp_file)
  #linesfound=$1
  linesfound=`cat $record_file|wc -l`

   case `echo $linesfound` in
   0)    echo "Sorry, nothing found\n"
         get_return
         return 0
         ;;
   *)    echo "Found the following\n"
         cat $record_file ;;
        esac
 printf "Type the books titel which you want to delete\n"
 read searchstr

  if [ "$searchstr" = "" ]; then
      return 0
   fi
 grep -v "$searchstr" $record_file > $temp_file
 mv $temp_file $record_file
 printf "Customer Record has been removed\n"
 get_return
return
}

view_books(){
printf "List of Customers are\n"

cat $record_file
get_return
return
}



edit_books(){

printf "list of Customers are\n"
cat $record_file
printf "Type the Name of customer you want to edit\n"
read searchstr
  if [ "$searchstr" = "" ]; then
     return 0
  fi
  grep -v "$searchstr" $record_file > $temp_file
  mv $temp_file $record_file
printf "Enter the new record"
add_books

}

rm -f $temp_file
if [!-f $record_file];then
touch $record_file
fi

clear
printf '\n\n\n'
printf 'HOTEL MANAGEMENT SYSTEM'
sleep 1

quit="n"
while [ "$quit" != "y" ];
do
 
#funtion call for choice
set_menu_choice
case "$menu_choice" in
a) add_books;;
b) find_books;;
c) edit_books;;
d) remove_books;;
e) view_books;;
f) quit=y;;
*) printf "Sorry, choice not recognized";;
esac
done
# Tidy up and leave

rm -f $temp_file
echo "THANK YOU"

exit 0
