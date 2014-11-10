#include <registryFunction.h>
#include <epicsExport.h>
#include <aSubRecord.h>
#include <stdio.h>

static long interp1d(aSubRecord *prec) {
  char *u;
  double *a, *e, *vala;
  double x_start, x_step, x_n, frac, r;
  long n;

  /* 
   * This routine does the 1d interpolation. The format of the waveform
   * wf[0] = number of elements
   * wf[1] = x start
   * wf[2] = x step
   *
   * a is the input value
   * e is the interp table
   */

  a = (double *)prec->a;
  u = (char *)prec->u;

  switch(*u){
    case 1:
      e = (double *)prec->e;
      break;
    case 2:
      e = (double *)prec->f;
      break;
    case 3:
      e = (double *)prec->g;
      break;
    case 4:
      e = (double *)prec->h;
      break;
    case 5:
      e = (double *)prec->i;
      break;
    case 6:
      e = (double *)prec->j;
      break;
    case 7:
      e = (double *)prec->k;
      break;
    case 8:
      e = (double *)prec->l;
      break;
    case 9:
      e = (double *)prec->m;
      break;
    case 10:
      e = (double *)prec->n;
      break;
    default:
      return 1;
      break;
  }
  vala = (double *)prec->vala;

  x_start = e[0];
  x_step = e[1];
  x_n = e[2];

  frac = ((a[0] - x_start) / x_step);
  n = (long)frac;
  r = frac - n;
  if((n < 0) || (n > (x_n-1))){
    return 2;
  }

  vala[0] = (e[n+4] - e[n+3]) * r;
  vala[0] = vala[0] + e[n+3];
  return 0; /* process output links */
}

epicsRegisterFunction(interp1d);
