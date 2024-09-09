from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
from decimal import Decimal
from .models import OrderGrabbing
from .serializers import  OrderGrabbingSerializer



class OrderGrabbingViewSet(viewsets.ModelViewSet):
    queryset = OrderGrabbing.objects.all()
    serializer_class = OrderGrabbingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user

        original_balance = Decimal(user.balance) 
        if user.level == "VIP1" and  user.balance > 700:
            if user.balance < 699:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

            if user.grabbed_orders_count > 2:
                return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)
            
            if user.grabbed_orders_count == 0:
                user.balance = original_balance - Decimal(700) 
            elif user.grabbed_orders_count == 1:
                user.balance = original_balance - Decimal(800) 
            elif user.grabbed_orders_count == 2:
                user.balance = original_balance - Decimal(1000) 
    
            user.grabbed_orders_count + 1

            # Calculate commission (20% of order price)

            commission_amount = Decimal(12)  # Ensure commission_amount is a Decimal
            today = timezone.now().date()  # Get today's date

            # Check the last order grabbing day
            last_grab_day = None
            if user.ordergrabbing_set.exists():
                last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

            # Update user's commission based on the day
            if last_grab_day is None or last_grab_day == today:
                if user.grabbed_orders_count == 0:
                    user.commission2 += Decimal(140)

                elif user.grabbed_orders_count == 1:
                    user.commission2 += Decimal(160)
                else:
                    user.commission2 += Decimal(200)
            else:
                if user.grabbed_orders_count == 0:
                    user.commission1 += Decimal(140)
                elif user.grabbed_orders_count == 1:
                    user.commission1 += Decimal(160)
                else:
                    user.commission1 += Decimal(200)
            
            if  user.grabbed_orders_count == 0:
                user.unsettle += Decimal(700) +  Decimal(140)
            elif  user.grabbed_orders_count == 1:
                user.unsettle += Decimal(800) +  Decimal(160)
            else:
                user.unsettle +=  Decimal(1000) +  Decimal(200)

            user.save()

            # Create order grabbing record
            grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
            serializer = self.get_serializer(grabbing)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        elif user.level == "VIP2" and  user.balance > 0:
            grab_amount = Decimal(3500)
            if user.balance < grab_amount - 1:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

            if user.grabbed_orders_count >= 2:
                return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)
            
            if user.grabbed_orders_count == 0:
                user.balance = original_balance - Decimal(9500) 
            elif user.grabbed_orders_count == 1:
                user.balance = original_balance - grab_amount
    
            user.grabbed_orders_count + 1

            # Calculate commission (20% of order price)

            commission_amount = Decimal(2850)  # Ensure commission_amount is a Decimal
            today = timezone.now().date()  # Get today's date

            # Check the last order grabbing day
            last_grab_day = None
            if user.ordergrabbing_set.exists():
                last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

            # Update user's commission based on the day
            if last_grab_day is None or last_grab_day == today:
                if user.grabbed_orders_count == 0:
                    user.commission2 += Decimal(2850)
                else:
                    user.commission2 += Decimal(1050)
            else:
                if user.grabbed_orders_count == 0:
                    user.commission1 += Decimal(1050)
                else:
                    user.commission1 += Decimal(2850)
            
            if  user.grabbed_orders_count == 0:
                user.unsettle = Decimal(9500) +  Decimal(2850)
            else:
                user.unsettle += grab_amount +  Decimal(1050)

            user.save()

            # Create order grabbing record
            grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
            serializer = self.get_serializer(grabbing)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        elif user.level == "VIP3" and  user.balance > 0:
            grab_amount = Decimal(15500)
            # commission_amount = Decimal(6220)  # Ensure commission_amount is a Decimal
            if user.balance < grab_amount - 1:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

            if user.grabbed_orders_count >= 12:
                return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)

            match user.grabbed_orders_count:
                case 0:
                    user.balance = original_balance - Decimal(15550)
                    user.unsettle = Decimal(15550) +  Decimal(6220)
                    commission_amount  = Decimal(6220)

                case 1:
                    user.balance = original_balance - Decimal(25350)
                    user.unsettle = Decimal(user.unsettle) + Decimal(25350) + Decimal(10140)
                    commission_amount  =  Decimal(10140)
                case 2:
                    user.balance = original_balance - Decimal(44500)
                    user.unsettle = Decimal(user.unsettle) + Decimal(44500) + Decimal(17800)
                    commission_amount  =  Decimal(17800)
                case 3:
                    user.balance = original_balance - Decimal(78600)
                    user.unsettle = Decimal(user.unsettle) + Decimal(78600) + Decimal(31440)
                    commission_amount  =  Decimal(31440)
                case 4:
                    user.balance = original_balance - Decimal(109320)
                    user.unsettle = Decimal(user.unsettle) + Decimal(109320) + Decimal(43728)
                    commission_amount  =  Decimal(43728)
                case 5:
                    user.balance = original_balance - Decimal(170450)
                    user.unsettle = Decimal(user.unsettle) + Decimal(170450) + Decimal(68180)
                    commission_amount  =  Decimal(68180)
                case 6:
                    user.balance = original_balance - Decimal(250000)
                    user.unsettle = Decimal(user.unsettle) + Decimal(250000) + Decimal(100000)
                    commission_amount  =  Decimal(100000)
                case 7:
                    user.balance = original_balance - Decimal(370400)
                    user.unsettle = Decimal(user.unsettle) + Decimal(370400) + Decimal(148160)
                    commission_amount  =  Decimal(148160)
                case 8:
                    user.balance = original_balance - Decimal(435200)
                    user.unsettle = Decimal(user.unsettle) + Decimal(435200) + Decimal(174080)
                    commission_amount  =  Decimal(174080)
                case 9:
                    user.balance = original_balance - Decimal(510550)
                    user.unsettle =Decimal(user.unsettle) +  Decimal(510550) + Decimal(204220)
                    commission_amount  =  Decimal(204220)
                case 10:
                    user.balance = original_balance - Decimal(530400)
                    user.unsettle = Decimal(user.unsettle) + Decimal(530400) + Decimal(212160)
                    commission_amount  =  Decimal(212160)
                case 11:
                    user.balance = original_balance - Decimal(610000)
                    user.unsettle = Decimal(user.unsettle) + Decimal(610000) + Decimal(244000)
                    commission_amount  =  Decimal(244000)
                case _:
                    pass

            # user.grabbed_orders_count += 1

            # Calculate commission (20% of order price)
           
            today = timezone.now().date()  # Get today's date

            # Check the last order grabbing day
            last_grab_day = None
            if user.ordergrabbing_set.exists():
                last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

            # Update user's commission based on the day
            if last_grab_day is None or last_grab_day == today:
                user.commission2 += commission_amount
            else:
                user.commission1 += commission_amount
            user.save()

            # Create order grabbing record
            grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
            serializer = self.get_serializer(grabbing)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            # Add a fallback response in case none of the conditions match
            return Response({"error": "Invalid operation or user level"}, status=status.HTTP_400_BAD_REQUEST)