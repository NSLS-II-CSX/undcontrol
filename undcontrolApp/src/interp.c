#include <registryFunction.h>
#include <epicsExport.h>
#include <aSubRecord.h>
#include <stdio.h>

static long interp1d(aSubRecord *prec) {
  /* 
   * This routine does the 2d interpolation. The format of the waveform
   * wf[0] = number of elements in x 
   * wf[1] = x start
   * wf[2] = x step
   * wf[3] = number of elements in y
   * wf[4] = y start
   * wf[5] = y step
   *
   * a is the 1st input value
   * b is the 2nd input value
   * c is the 1st offset correction
   * d is the 2nd offset correction
   * e is the 1st interp table
   *
   * vala is the 1st output value
   */

  /* Get the interp table based on the table setting */
  double *wfrm;

  //fprintf(stderr, "table = %d\n", *((int *)prec->u));

  switch(*((int *)prec->u)){
    case 1:
      wfrm = (double *)prec->e;
      break;
    case 2:
      wfrm = (double *)prec->f;
      break;
    case 3:
      wfrm = (double *)prec->g;
      break;
    case 4:
      wfrm = (double *)prec->h;
      break;
    case 5:
      wfrm = (double *)prec->i;
      break;
    case 6:
      wfrm = (double *)prec->j;
      break;
    case 7:
      wfrm = (double *)prec->k;
      break;
    case 8:
      wfrm = (double *)prec->l;
      break;
    case 9:
      wfrm = (double *)prec->m;
      break;
    case 10:
      wfrm = (double *)prec->n;
      break;
    default:
      return 1;
      break;
  }

  double x_in  = ((double *)prec->a)[0];
  double y_in  = ((double *)prec->b)[0];
  double x_off = ((double *)prec->c)[0];
  double y_off = ((double *)prec->d)[0];

  double x_start = wfrm[0];
  double x_step  = wfrm[1];
  long   x_n     = (long)wfrm[2];
  double y_start = wfrm[3];
  double y_step  = wfrm[4];
  long   y_n     = (long)wfrm[5];
  double *table  = wfrm + 6;

  //fprintf(stderr, "x_in = %f\n", x_in);
  //fprintf(stderr, "y_in = %f\n", y_in);
  //fprintf(stderr, "x_start = %f\n", x_start);
  //fprintf(stderr, "x_step = %f\n", x_step);
  //fprintf(stderr, "x_n = %ld\n", x_n);
  //fprintf(stderr, "y_start = %f\n", y_start);
  //fprintf(stderr, "y_step = %f\n", y_step);
  //fprintf(stderr, "y_n = %ld\n", y_n);
  
  double _x = (((x_in + x_off) - x_start) / x_step);
  double _y = (((y_in + y_off) - y_start) / y_step);

  //fprintf(stderr, "_x = %f , _y = %f\n", _x, _y);

  if((_x < 0) || (_x >= (x_n - 1))){
    /* Table out of bounds */
    return 2;
  }
  if((_y < 0) || (_y >= (y_n - 1))){
    /* Table out of bounds */
    return 2;
  }
  
  long x = (long)_x;
  long y = (long)_y;
  double x_r = _x - x;
  double y_r = _y - y;

  //fprintf(stderr, "x = %ld, y = %ld, x_r = %f, y_r = %f\n", x, y, x_r, y_r);

  long ind = x + (y * y_n);
  double r1 = table[ind] + ((table[ind+1] - table[ind]) * x_r);
  double r2 = table[ind + x_n] + ((table[ind+1+x_n] - table[ind+x_n]) * x_r);

  // fprintf(stderr ,"r1 = %f, r2 = %f\n", r1, r2);

  double *out = (double *)prec->vala;
  *out = r1 + ((r2 - r1) * y_r);
  
  //fprintf(stderr, "Out == %f\n", *out);
  //
  return 0; /* process output links */
}

epicsRegisterFunction(interp1d);
