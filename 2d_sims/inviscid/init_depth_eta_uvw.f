          parameter(m=1000,n=1, k=10)
          real eta(m,n), depth(m,n), u(m,n,k), v(m,n,k)
          real hNorm, uNorm, So
          real dx, dy
          
          hNorm = 0.00798
          uNorm = 1.038
          So = 0.05011

          dx = 0.01

          ! creation of depth.txt
          do j=1,n
          do i=1,m
            depth(i,j) = hNorm+So*(i-0.50)*dx
          enddo
          enddo

          open(2,file='depth.txt')
          do j=1,n
            write(2,1000)(depth(i,j),i=1,m)
          enddo
1000       format(1000f12.5)

          ! creation of eta0.txt


          ! creation of uvw0.txt



!           do j=1,n
!           do i=1,m
!             eta(i,j)=0.0
! c             eta(i,j)=0.0
!             u(i,j)=uNorm
!             v(i,j)=0.0
!           enddo
!           enddo

!           open(2,file='eta.txt')
!           do j=1,n
!             write(2,100)(eta(i,j),i=1,m)
!           enddo
! 100       format(1000f12.5)

!           close(2)
          
!           open(3,file='u.txt')
!           do j=1,n
!             write(3,200)(u(i,j),i=1,m)
!           enddo
! 200       format(1000f12.5)

!           close(3)
          
!           open(4,file='v.txt')
!           do j=1,n
!             write(4,300)(v(i,j),i=1,m)
!           enddo
! 300       format(1000f12.5)

!           close(4)


          end

          
