JsOsaDAS1.001.00bplist00�Vscripto
� O b j C . i m p o r t ( " C o c o a " ) ; 
 
 v a r   a p p   =   A p p l i c a t i o n . c u r r e n t A p p l i c a t i o n ( ) 
 a p p . i n c l u d e S t a n d a r d A d d i t i o n s   =   t r u e ; 
 
 y t D o w n l o a d e r   =   a p p . p a t h T o R e s o u r c e ( " y o u t u b e - d l " ) 
 
 
 v a r   s t y l e M a s k   =   $ . N S T i t l e d W i n d o w M a s k   |   $ . N S C l o s a b l e W i n d o w M a s k   |   $ . N S M i n i a t u r i z a b l e W i n d o w M a s k ; 
 v a r   w i n d o w H e i g h t   =   1 2 5 ; 
 v a r   w i n d o w W i d t h   =   6 0 0 ; 
 v a r   c t r l s H e i g h t   =   8 0 ; 
 v a r   m i n W i d t h   =   4 0 0 ; 
 v a r   m i n H e i g h t   =   3 4 0 ; 
 v a r   w i n d o w   =   $ . N S W i n d o w . a l l o c . i n i t W i t h C o n t e n t R e c t S t y l e M a s k B a c k i n g D e f e r ( 
     $ . N S M a k e R e c t ( 0 ,   0 ,   w i n d o w W i d t h ,   w i n d o w H e i g h t ) , 
     s t y l e M a s k , 
     $ . N S B a c k i n g S t o r e B u f f e r e d , 
     f a l s e 
 ) ; 
 
 v a r   t e x t F i e l d L a b e l   =   $ . N S T e x t F i e l d . a l l o c . i n i t W i t h F r a m e ( $ . N S M a k e R e c t ( 2 5 ,   ( w i n d o w H e i g h t   -   4 0 ) ,   2 0 0 ,   2 4 ) ) ; 
 t e x t F i e l d L a b e l . s t r i n g V a l u e   =   " P a s t e   o r   d r a g   a   Y o u t u b e   l i n k   h e r e : " ; 
 t e x t F i e l d L a b e l . d r a w s B a c k g r o u n d   =   f a l s e ; 
 t e x t F i e l d L a b e l . e d i t a b l e   =   f a l s e ; 
 t e x t F i e l d L a b e l . b e z e l e d   =   f a l s e ; 
 t e x t F i e l d L a b e l . s e l e c t a b l e   =   t r u e ; 
 
 v a r   t e x t F i e l d   =   $ . N S T e x t F i e l d . a l l o c . i n i t W i t h F r a m e ( $ . N S M a k e R e c t ( 2 5 ,   ( w i n d o w H e i g h t   -   6 0 ) ,   4 0 5 ,   2 4 ) ) ; 
 t e x t F i e l d . e d i t a b l e   =   f a l s e ; 
 
 v a r   b t n   =   $ . N S B u t t o n . a l l o c . i n i t W i t h F r a m e ( $ . N S M a k e R e c t ( ( w i n d o w W i d t h   -   1 6 0 ) ,   ( w i n d o w H e i g h t   -   6 2 ) ,   1 5 0 ,   2 5 ) ) ; 
 b t n . t i t l e   =   " D o w n l o a d " ; 
 b t n . b e z e l S t y l e   =   $ . N S R o u n d e d B e z e l S t y l e ; 
 b t n . b u t t o n T y p e   =   $ . N S M o m e n t a r y L i g h t B u t t o n ; 
 
 v a r   p r o g B a r   =   $ . N S P r o g r e s s I n d i c a t o r . a l l o c . i n i t W i t h F r a m e ( $ . N S M a k e R e c t ( ( w i n d o w W i d t h   /   4 ) ,   ( w i n d o w H e i g h t   -   1 0 0 ) ,   ( w i n d o w W i d t h   /   2 ) ,   2 5 ) ) ; 
 p r o g B a r . i n d e t e r m i n a t e   =   f a l s e ; 
 p r o g B a r . d i s p l a y W h e n S t o p p e d   =   f a l s e ; 
 p r o g B a r . u s e s T h r e a d e d A n i m a t i o n   =   t r u e ; 
 
 w i n d o w . c o n t e n t V i e w . a d d S u b v i e w ( t e x t F i e l d L a b e l ) ; 
 w i n d o w . c o n t e n t V i e w . a d d S u b v i e w ( t e x t F i e l d ) ; 
 w i n d o w . c o n t e n t V i e w . a d d S u b v i e w ( b t n ) ; 
 
 
 w i n d o w . c e n t e r ; 
 w i n d o w . t i t l e   =   " Y o u t u b e   D o w n l o a d e r " ; 
 w i n d o w . m a k e K e y A n d O r d e r F r o n t ( w i n d o w ) ; 
 
 r a w L o g P a t h   =   " / v a r / t m p / y o u t u b e - d l . l o g " 
 o u t p u t P a t h   =   " ~ / D e s k t o p / " 
 p a t h   =   P a t h ( r a w L o g P a t h ) ; 
 v a r   r e g   =   ' ( \ \ d + ( \ \ . \ \ d + ) ? | \ \ . \ \ d + )   ? % ' 
 
 v a r   c m d O p t s   =   [ ' - - n o - p l a y l i s t ' ,   ' - - n e w l i n e ' ,   ' - o ' ] ; 
 v a r   c m d S t r i n g   =   ' / u s r / b i n / n o h u p '   +   a p p . p o s i x P a t h ( y t D o w n l o a d e r ) ; 
 
 a p p . d i s p l a y D i a l o g ( c m d S t r i n g ) ; 
 
 a p p . d o S h e l l S c r i p t ( " / u s r / b i n / n o h u p "   +   y t D o w n l o a d e r   +   "   - - n o - p l a y l i s t   "   +   "   - - n e w l i n e "   +   "   - o   "   &   o u t p u t P a t h   +   "   "   +   " "   +   "   & >   / v a r / t m p / y o u t u b e - d l . l o g " ) 
 
 
 v a r   s h o w P r o g r e s s   =   f u n c t i o n ( ) { 
 	 P r o g r e s s . d e s c r i p t i o n   =     " D o w n l o a d   i n   p r o g r e s s . . . " 
 	 P r o g r e s s . a d d i t i o n a l D e s c r i p t i o n   =   " P r e p a r i n g & " 
 	 d e l a y ( 2 ) 
 	 P r o g r e s s . t o t a l U n i t C o u n t   =   1 0 0 ; 
 	 v a r 	 p e r c e n t a g e   =   0 . 0 
 	 
 	 w h i l e   ( p e r c e n t a g e   <   9 9 )   { 
 	 	 v a r   o u t p u t   =   a p p . d o S h e l l S c r i p t ( " / u s r / b i n / t a i l   - 1 "   +   "   "   +   r a w L o g P a t h ) ; 
 	 	 v a r   p e r c e n t a g e   =   o u t p u t . m a t c h ( r e g ) [ 0 ] 
 	 	 p e r c e n t a g e   =   p e r c e n t a g e . s p l i t ( ' % ' ) . j o i n ( ' ' ) 
         	 P r o g r e s s . a d d i t i o n a l D e s c r i p t i o n   =   o u t p u t 
 	         P r o g r e s s . c o m p l e t e d U n i t C o u n t   =   p e r c e n t a g e 
         	 d e l a y ( 0 . 1 ) 
 	 } 
 
 } 
 
 s h o w P r o g r e s s ( ) ; 
 
 
 / / p e r c e n t a g e :   |   g r e p   ' \ [ d o w n l o a d \ ] '   |   c u t   - f 2   - d "   " 
 / / t o t a l   s i z e :   |   g r e p   ' \ [ d o w n l o a d \ ] '   |   c u t   - f 4   - d "   " 
 / / d l   s p e e d :       |   
 / / e t a : 	 	     |   a w k   - F   "   "   ' { p r i n t   $ N F } ' 
                              �jscr  ��ޭ